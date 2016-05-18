#! /usr/bin/env python
def run():
    from fancy_site import app
    app.run()

if __name__ == "__main__":
    from fancy_site.views.main import *
    run()
