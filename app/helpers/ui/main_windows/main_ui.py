from app.helpers.ui.helpers.base import base_ui


class main_window(base_ui):
    def __init__(self, window_title, title, buttons, menu):
        super(main_window, self).__init__(
            window_title=window_title, title=title, menu=menu, logo=False
        )
