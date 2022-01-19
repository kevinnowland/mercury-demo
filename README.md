# Mercury test

This is a test of [mercury](https://github.com/mljar/mercury), which is a
way to use Jupyter notebooks as semi-interactive dashboards. It could be
useful for showcasing a small project, as the interface which it develops is
split in half, with the left side containing parameters for the notebook
and the right side displaying notebook contents, either hiding the cells
and just showing outputs or including the cells as well.

The big con is that when changing parameters, the notebook reloading process
is extremely slow. In my opinion, the present state of mercury is fine for 
proof of conceept / demonstration purposes but not yet suitable for production
dashboarding.


## Running locally


1. `git clone` this repository and `cd` into it.
1. Install requirements in your virtual environment of choice (for me this meant
running `python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt`).
2. Confirm the notebook is working by running `jupyter notebook` and ensuring that all
cells can run. Feel free to shut down the notebook, it does not have to be running
for mercury to work.
2. Add the notebook to mercury with `mercury add iris-test.ipynb`. Note that mercury
is sort of a page of dashboards where each dashboard corresponds to a notebook, so you
can run more than one notebook.
3. Start the server with `mercury runserver --runworker`
4. Go to `http://127.0.0.1:8000` and click on the notebook to see that it works.


## Running on heroku


We are following the instructions from [this tutorial](https://mljar.com/blog/share-jupyter-notebook-as-web-app/)
Step 0 is to create a heroku account and install the CLI.

I found this to be rather unstable. I pushed a notebook that worked fine locally
and it updated on the app but then just hung with the logs not telling me much.

1. Clone this repository and `cd` into it.
1. Run `heroku login` 
2. Run `heroku create APPNAME` where you fill in whatever `APPNAME` you want.
2. Set heroku environment variables:

    ```bash
    heroku config:set SERVE_STATIC=True
    heroku config:set ALLOWED_HOSTS=APPNAME.herokuapp.com
    heroku config:set NOTEBOOKS=iris-test.ipynb
    ```
4. run `git push heroku main`
5. Start the app with`heroku ps:scale web=1` and confirm the
app is working by running `heroku open` to open the app in a browser.
5. Shut down the running app with `heroku ps:scale web=0`
6. Destroy the app with `heroku apps:destroy APPNAME --confrim APPNAME`.

To view logs, run `heroku logs --tail`.
