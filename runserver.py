#! /usr/bin/env python
def run():
    from empty_flask import app
    app.run()

if __name__ == "__main__":
    from empty_flask.views.main import *
    run()
