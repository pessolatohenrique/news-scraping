class Subject:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self.name

    def show_label(self):
        print(f"Assunto pesquisado: {self._name}")