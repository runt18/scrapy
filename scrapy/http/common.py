def obsolete_setter(setter, attrname):
    def newsetter(self, value):
        c = self.__class__.__name__
        msg = "{0!s}.{1!s} is not modifiable, use {2!s}.replace() instead".format(c, attrname, c)
        raise AttributeError(msg)
    return newsetter
