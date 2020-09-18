def x(
        name,
        last_name=None,
        address=None
):
    if address:
        return True
    elif last_name:
        return last_name
    return name


def y(name):
    return ord(name[0])


class Test:
    @staticmethod
    def speak(word):
        print(word)
        return word
