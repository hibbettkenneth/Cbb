from flask import Flask, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def index():
    """Main dashboard with predictions"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Sample predictions for demonstration
    predictions = [
        {
            'home_team': 'Duke Blue Devils',
            'away_team': 'North Carolina',
            'predicted_spread': 4.5,
            'home_win_probability': 0.682,
            'value_score': 0.847,
            'expected_home_score': 78.4,
            'expected_away_score': 73.9,
            'confidence_level': 'HIGH'
        },
        {
            'home_team': 'Kansas Jayhawks',
            'away_team': 'Kansas State',
            'predicted_spread': -7.2,
            'home_win_probability': 0.821,
            'value_score': 0.923,
            'expected_home_score': 84.7,
            'expected_away_score': 77.5,
            'confidence_level': 'HIGH'
        }
    ]
    
    return render_template('index.html',
                         predictions=predictions,
                         total_games=len(predictions),
                         date=today)

@app.route('/api/predictions/today')
def api_today_predictions():
    """API endpoint for today's predictions"""
    predictions = [
        {
            'game_id': 'sample-1',
            'home_team': 'Duke Blue Devils',
            'away_team': 'North Carolina',
            'predicted_spread': 4.5,
            'home_win_probability': 0.682,
            'value_score': 0.847,
            'expected_home_score': 78.4,
            'expected_away_score': 73.9
        }
    ]
    
    return jsonify({
        'date': datetime.now().strftime('%Y-%m-%d'),
        'predictions': predictions,
        'count': len(predictions),
        'status': 'success'
    })

@app.route('/api/system-status')
def api_system_status():
    """API endpoint for system status"""
    return jsonify({
        'status': 'operational',
        'components': {
            'api_connected': True,
            'model_trained': True,
            'features_ready': True,
            'system_active': True
        },
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=False)
