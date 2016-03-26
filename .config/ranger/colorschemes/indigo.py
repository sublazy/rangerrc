# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Indigo(ColorScheme):
    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            pass

        elif context.in_browser:
            if context.selected:
                attr = normal
                bg = black
            if context.directory:
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= normal
                if context.link:
                    fg = cyan
                if context.directory:
                    attr |= bold
                elif context.executable:
                    fg = green
                if context.marked:
                    attr |= bold
                    fg = yellow

        elif context.highlight:
            attr |= reverse

        elif context.in_titlebar and context.tab and context.good:
            attr |= reverse

        elif context.in_statusbar:
            if context.loaded:
                attr |= reverse
            if context.marked:
                attr |= reverse

        elif context.in_taskview:
            if context.selected:
                attr |= bold
            if context.loaded:
                attr |= reverse

        return fg, bg, attr
