from flask import Flask, send_file

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/favicon.ico')
def favicon():
    return send_file(
        b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAdgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADLSURBVDiNpZIxCsJAEEXfJqQQFAsxrS3Y2HkCC0/gDSw9hKVgK4g3sPEI2go2dqJBIbiQZDO7i6BkYcDKwjDM5zPznxHvPZ1ijEGrgHZgA3w6sIAVMBTvPZ0TRVEG3ICRqgKuwFycc1RVFQBnYKKqADNgI865BqCqKmAHTFUVYAPsxTnXAFRVBeyBuaoC7ICjOOcaQBRFGbAHFqoKsAFO4pxrALqu6w1wBqaqCrAELuKcawD6vp8AF2ChqgBz4CbOuQYQBMEEuAFLVQWYAndxzjUAY8wIuANrVQWYAA9xzjUAY8wQeABbVQUYAk9xzjUAY0wKPIHdH6pz4CXOuQbwBdKEE5CjFQSjAAAAAElFTkSuQmCC',
        mimetype='image/x-icon'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)
