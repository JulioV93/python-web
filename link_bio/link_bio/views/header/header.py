import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Julio Machado",
                size="6"
            ),
            rx.vstack(
                rx.heading(
                    "Julio Machado",
                    size="4",
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@JulioV93",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/"),
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/"),
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/"),
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/"),
                ),
                align_items="start"
            ),
            spacing="4",
        ),
        rx.flex(
            info_text("+6", "años de experiencia"),
            rx.spacer(),
            info_text("+6", "años de experiencia"),
            rx.spacer(),
            info_text("+6", "años de experiencia"),
            rx.spacer(),
            width="100%"
        ),
        rx.text(
            "Ingeniero en Software e informática, con una sólida formación en el desarrollo de sistemas y aplicaciones. Cuento con más de 5 años de experiencia en la resolución de desafíos tecnológicos utilizando javascript, PHP, python, AzureDevOps, GIT, Bitbucket.",
            color=TextColor.BODY.value
        ),
        spacing="4",
        align_items="start"
    )