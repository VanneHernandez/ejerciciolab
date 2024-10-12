class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BynarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node (value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node, value)

    def preorden(self, nodo):
        if nodo is not None:
            #RAIZ
            print(nodo.valor, end= "")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end="")
            self.inorden(nodo.derecho)
    def posorden(self, nodo):
        if nodo is not None:
            
