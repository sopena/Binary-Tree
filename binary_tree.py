class Arvore:
    def __init__(self, dado):
        self.esq = None
        self.dado = dado
        self.dir = None

    def imprimirPreEsq(self):
        print(self.dado)
        if self.esq:
            self.esq.imprimirPreEsq()
        if self.dir:
            self.dir.imprimirPreEsq()

    def imprimirPreDir(self):
        print(self.dado)
        if self.dir:
            self.dir.imprimirPreDir()
        if self.esq:
            self.esq.imprimirPreDir()

    def imprimirInDir(self):
        if self.dir:
            self.dir.imprimirInDir()
        print(self.dado)
        if self.esq:
            self.esq.imprimirInDir()

    def imprimirInEsq(self):
        if self.esq:
            self.esq.imprimirInEsq()
        print(self.dado)
        if self.dir:
            self.dir.imprimirInEsq()
    
    def imprimirPosEsq(self):
        if self.esq:
            self.esq.imprimirPosEsq()
        if self.dir:
            self.dir.imprimirPosEsq()
        print(self.dado)
    
    def imprimirPosDir(self):
        if self.dir:
            self.dir.imprimirPosDir()
        if self.esq:
            self.esq.imprimirPosEsq()
        print(self.dado)

    def localizar(self, v):
        if v == self.dado:
            return self
        if self.esq:
            aux = self.esq.localizar(v)
            if aux:
                return aux
        if self.dir:
            aux = self.dir.localizar(v)
            if aux:
                return aux
        else:
            return None

    def imprimir(self, lado, metodo):
        if lado == "esq" and metodo == "pre":
            self.imprimirPreEsq()
        if lado == "dir" and metodo == "pre":
            self.imprimirPreDir()
        if lado == "esq" and metodo == "in":
            self.imprimirInEsq()
        if lado == "dir" and metodo == "in":
            self.imprimirInDir()
        if lado == "esq" and metodo == "pos":
            self.imprimirPosEsq()
        if lado == "dir" and metodo == "pos":
            self.imprimirPosDir()
    
    def inserir(self, pai, lado, filho):
        pai = self.localizar(pai)
        if lado == "esq":
            if pai.esq == None:
                pai.esq = Arvore(filho)
                print("Adicionado com sucesso!")
            else: print("Já existe um nodo nesse lugar")
        if lado == "dir":
            if pai.dir == None:
                pai.dir = Arvore(filho)
                print("Adicionado com sucesso!")
            else: print("Já existe um nodo nesse lugar")
    
    def localizar_pai(self, v):
        if v == self.dado:
            return self
        if self.esq:
            aux = self.esq.localizar(v)
            if aux:
                return aux
        if self.dir:
            aux = self.dir.localizar(v)
            if aux:
                return aux
        else:
            return None
        

a = Arvore("A")
a.esq = Arvore("B")
a.esq.dir = Arvore("G")
a.esq.esq = Arvore("D")
a.esq.esq.esq = Arvore("F")
a.esq.esq.dir = Arvore("E")
a.dir = Arvore("C")
#a.imprimir("esq", "pre")
#pai = a.localizar("G")
#if pai == None:
#    print("Esse valor não está na árvore")
#else: 
#    print(pai.dado)

a.inserir("C", "dir", "H")
a.inserir("H", "esq", "W")
a.imprimir("esq", "pre")