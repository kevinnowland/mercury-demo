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


1. `git clone` this repository
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


Step 0 is to create a heroku account and install the CLI.

1. Create a fork of this repository for yourself. Then clone and
enter into it the folder.
1. Run `heroku login` 
2. Run `heroku create`
3. Confirm app runs locally with `heroku local web` and browsing to `http://127.0.0.1:8000`.
4. run `git push heroku main`
5. Start the app with`heroku ps:scale web=1` and confirm the
app is working by running `heroku open` to open the app in a browser.
5. Shut down the running app with `heroku ps:scale web=0`
