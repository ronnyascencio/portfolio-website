"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .components import banner
from .pages import home


class State(rx.State):
    """The app state."""

    ...


# def index():
#     return home()


app = rx.App()
app.add_page(home, route="/", title="Home")
