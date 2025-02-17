import reflex as rx


class TopBannerNewsletter(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
            rx.flex(
                rx.text(
                    "Join our newsletter",
                    text_wrap="nowrap",
                    weight="medium",
                ),
                rx.input(
                    rx.input.slot(rx.icon("mail")),
                    rx.input.slot(
                        rx.icon_button(
                            rx.icon(
                                "arrow-right",
                                padding="0.15em",
                            ),
                            cursor="pointer",
                            radius="large",
                            size="2",
                            justify="end",
                        ),
                        padding_right="0",
                    ),
                    placeholder="Your email address",
                    type="email",
                    size="2",
                    radius="large",
                ),
                rx.icon(
                    "x",
                    cursor="pointer",
                    justify="end",
                    flex_shrink=0,
                    on_click=cls.toggle,
                ),
                wrap="nowrap",
                # position="fixed",
                flex_direction=["column", "row", "row"],
                justify_content=["start", "space-between"],
                width="100%",
                # top="0",
                spacing="2",
                align_items=["start", "center", "center"],
                left="0",
                # z_index="50",
                padding="1rem",
                background=rx.color("accent", 4),
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )


top_banner_newsletter = TopBannerNewsletter.create
