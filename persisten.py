import pickle

def load():
    with open('mypickle.pk', 'rb') as fi:
        nota = pickle.load(fi)
        return nota


def save(x,text):
    nota = load()
    nota[x] = text
    with open('mypickle.pk', 'wb') as fi:
        pickle.dump(nota, fi)
