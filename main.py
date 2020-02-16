from Subject import Subject
from SiteContent import SiteContent

if (__name__ == "__main__"):
    choose_site = 0
    subject_input = input("Pesquise um assunto: ")

    while (choose_site <= 0 or choose_site > 3):
        choose_site = int(input("Escolha a fonte: (1) Tecmundo, (2) Omelete ou (3) G1: "))
        continue

    subject = Subject(subject_input)

    if (choose_site == 1):
        tecmundo_url = f'https://www.tecmundo.com.br/busca'
        tecmundo = SiteContent(subject, 'Tecmundo', tecmundo_url, 'tec--list__item', 'tec--card__title', 'a',
                               'tec--timestamp__item z--font-semibold')
        tecmundo.search()
    elif(choose_site == 2):
        omelete_url = f'https://www.omelete.com.br/busca'
        omelete = SiteContent(subject, 'Omelete', omelete_url, 'featured__head', 'mark__title', 'h2', 'mark__time')
        omelete.search()
    else:
        g1_url = f'https://g1.globo.com/busca/'
        g1 = SiteContent(subject, 'G1', g1_url, 'widget--info', 'widget--info__title', None, 'widget--info__meta')
        g1.search()





