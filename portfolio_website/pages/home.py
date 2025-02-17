import reflex as rx


@rx.page(route="/", title="Home")
def home():
    return rx.center(
        rx.center(
            rx.avatar(
                size="8",
            ),
            rx.flex(
                rx.link(
                    rx.button(
                        rx.icon("github"),
                        color_scheme="lime",
                    ),
                    href="https://github.com/ronnyascencio",
                ),
                rx.link(
                    rx.button(
                        rx.icon("linkedin"),
                        color_scheme="lime",
                    ),
                    href="https://linkedin.com/in/ronnyascencio",
                ),
                # rx.button(),
                spacing="4",
            ),
            direction="column",
            spacing="3",
        ),
        rx.box(
            rx.blockquote(
                rx.heading("Ronny Ascencio", size="4"),
                "I am a ",
                rx.text.strong("Python Developer & Digital Artist "),
                "based in Montreal, Canada.",
                "I always been in love of technology and creative media,",
                "I came from a Film and Tv industry passing trhough the VFX as an artist ",
                "and is there when I got inbolved with ",
                rx.text.strong("Python "),
                "developing tools for ",
                rx.text.strong("VFX."),
            ),
            width="35%",
            padding_left="2em",
        ),
        direction="row",
        padding_top="5em",
    ), rx.center(
        rx.button(
            "Read more",
        ),
        rx.button(
            "Curriculum",
        ),
        direction="row",
        spacing="4",
        padding_left="3em",
        padding_top="1em",
    )
