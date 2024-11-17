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
        
    def localizar_pai(self, v):
        if v == self.dado:
            return self
        if self.esq:
            if self.esq.dado == v:
                return self
            aux = self.esq.localizar_pai(v)
            if aux:
                return aux
        if self.dir:
            if self.dir.dado == v:
                print("funcionou")
                return self
            aux = self.dir.localizar_pai(v)
            if aux:
                return aux
        else:
            return None
        
    def excluir(self, v):
        pai = self.localizar_pai(v)
        if pai.esq != None:
            if pai.esq.dado == v:
                if pai.esq.esq != None:
                    pai.esq = pai.esq.esq
                if pai.esq.dir != None:
                    pai.esq = pai.esq.dir
                if pai.esq.esq == None and pai.esq.dir == None:
                    pai.esq = None
                print("excluido")
        if pai.dir != None:
            if pai.dir.dado == v:
                if pai.dir.dir != None:
                    pai.dir = pai.dir.dir
                if pai.dir.esq != None:
                    pai.dir = pai.dir.esq
                if pai.dir.dir == None and pai.dir.esq == None:
                    pai.dir = None
                print("excluido")
        
        

a = Arvore("A")
a.esq = Arvore("B")
a.esq.dir = Arvore("G")
a.esq.esq = Arvore("D")
a.esq.esq.esq = Arvore("F")
a.esq.esq.dir = Arvore("E")
a.dir = Arvore("C")
#a.imprimir("esq", "pre")
#nodo = a.localizar("G")
#if nodo == None:
#    print("Esse valor não está na árvore")
#else: 
#    print(nodo.dado)

a.inserir("C", "dir", "H")
a.inserir("H", "esq", "W")
#a.imprimir("esq", "pre")

pai_de_g = a.localizar_pai("W")

#a.excluir("H")
#a.excluir("C")
a.excluir("W")
a.imprimir("esq", "pre")