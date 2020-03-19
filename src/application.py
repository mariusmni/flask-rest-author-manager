from main import config
from main import create_app

if __name__ == "__main__":
    app = create_app(config)
    app.run()

