from app.helpers.ui.main_windows.main_ui import main_window

main_ui = None


def main_ui_window():
    global main_ui

    main_ui = main_window(
        window_title="GSTR Utilities",
        title="GST Utilities",
        buttons={
            "utility_buttons": [],
            "reco_buttons": [],
        },
        menu=True
    )

    main_ui.initialize_engine()


if __name__ == "__main__":
    main_ui_window()
