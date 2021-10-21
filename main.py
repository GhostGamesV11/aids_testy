from typing import Any

class Node:
    def __init__(self, value: Any = None, next = None):
        self.value: Any = value
        self.next: 'Node' = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None



    #umieści nowy węzeł na początku listy
    def push(self,value:Any) -> None:
        new = Node(value, self.head)
        self.head = new


    #umieści nowy węzeł na końcu listy
    def append(self,value:Any)-> None:
        if self.head is None:
            self.head = Node(value ,None)
            return
        a = self.head
        while a.next:
            a = a.next

        a.next = Node(value,None)


    #zwróci węzeł znajdujący się na wskazanej pozycji
    def node(self, at:int) -> Node:
        current = self.head
        count = 0
        while current is not None:
            if count == at:
                return current
            count +=1
            current = current.next



    # #wstawi nowy węzeł tuż za węzłem wskazanym w parametrze
    # def insert(self, value, after):
    #     a = self.head
    #     while a is not None:
    #         if after==a.value:
    #             break
    #         a = a.next
    #     if a is None:
    #         print("tego elementu nie ma na liscie")
    #     else:
    #         nowe = Node(value)
    #         nowe.next = a.next
    #         a.next = nowe

    #wstawi nowy węzeł tuż za węzłem wskazanym w parametrze v2
    def insert(self, value: Any, after: Node) ->None:
        node = Node(value)
        if after.next is not None:
            temp = after.next
            after.next = node
            node.next = temp
        else:
            after.next = node
            self.tail = node

    #usunie pierwszy element z listy i go zwróci
    # def pop(self) -> Any:
    #     if self.head is None:
    #         print("blad")
    #     else:
    #         print(f'element usuniety {self.head.value}')
    #         self.head = self.head.next

    #usunie ostatni element z listy i go zwróci
    # def remove_last(self) -> Any:
    #     if self.head is None:
    #         print("blad")
    #     else:
    #         a = self.head
    #         while a.next.next is not None:
    #             a = a.next
    #         print(f'element usuniety {a.next.value}')
    #         a.next = None

    #usunie z listy następnik węzła przekazanego w parametrze
    def remove(self,after):
        if self.head is None:
            print('lista jest pusta')
        if after==self.head.value:
            self.head = self.head.next
            return
        licznik = 0
        a = self.head
        while a:
             if licznik == after:
                  a.next = a.next.next
                  break

             a = a.next
             licznik += 1

    # usunie z listy następnik węzła przekazanego w parametrze v2
    # def remove(self, after):
    #     if self.head is None:
    #         print('lista jest pusta')
    #     if after == self.head.value:
    #         self.head = self.head.next
    #         return
    #     a = self.head
    #     while a.next is not None:
    #         if after == a.next.value:
    #             break
    #         a = a.next
    #     if a.next is None:
    #         print('nie ma takiej liczby')
    #     else:
    #         a.next = a.next.next
    #

    #usunie z listy następnik węzła przekazanego w parametrze
    # def remove(self,after: Node) -> Any:
    #     if after.next is None:
    #         return
    #     if after.next.next is not None:
    #         after.next = after.next.next
    #     else:
    #         after.next = None
    #         self.tail = after


    #wypisz v
    def print(self):
        # if self.head is None:
        #     print("lista jest pusta")
        #     return
        a = self.head
        b = ''
        while a:
            b += str(a.value)
            if a.next is not None:
                b += ' ---> '
            a = a.next
        print(b)

    #dlugosc
    def len(self):
        count = 0
        a = self.head
        while(a):
            count+=1
            a = a.next
        return print(f'ilosc elementow w liscie: {count}')



list_ = LinkedList()
list_.push(1)
list_.push(0)
list_.append(9)
list_.append(10)
# list_.remove_last()
list_.remove(2)
# list_.pop()
# list_.node()
# list_.insert(5,list_.node(1))
list_.print()
# list_.len()








