class Stack:
    # Конструктор класса, создает пустой список для хранения элементов стека
    def __init__(self):
        self.items = []  # Инициализация списка элементов

    # Метод проверки стека на пустоту
    def is_empty(self):
        return len(self.items) == 0  # Возвращает True, если список пуст

    # Метод добавления элемента на вершину стека
    def push(self, item):
        self.items.append(item)  # Добавление элемента в конец списка

    # Метод удаления и возврата верхнего элемента стека
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Удаление и возврат последнего элемента
        else:
            raise IndexError("pop from empty stack")  # Ошибка при попытке удаления из пустого стека

    # Метод просмотра верхнего элемента без удаления
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Возврат последнего элемента без удаления
        else:
            raise IndexError("peek from empty stack")  # Ошибка при попытке просмотра пустого стека

    # Метод получения размера стека
    def size(self):
        return len(self.items)  # Возврат количества элементов в стеке


# Функция проверки сбалансированности скобок
def is_balanced(brackets):
    stack = Stack()  # Создаем экземпляр стека для хранения открывающих скобок

    # Множество открывающих скобок
    opening_brackets = {'(', '[', '{'}

    # Словарь соответствия закрывающих скобок открывающим
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    # Проходим по каждому символу во входной строке
    for bracket in brackets:
        # Если символ - открывающая скобка
        if bracket in opening_brackets:
            stack.push(bracket)  # Добавляем в стек
        # Если символ - закрывающая скобка
        elif bracket in closing_brackets:
            # Если стек пуст или последняя открывающая не соответствует текущей закрывающей
            if stack.is_empty() or stack.pop() != closing_brackets[bracket]:
                return False  # Последовательность несбалансирована

    # Если после обработки всех скобок стек пуст - последовательность сбалансирована
    return stack.is_empty()



if __name__ == "__main__":

    test_cases = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]


    for test in test_cases:
        if is_balanced(test):
            print(f"Сбалансированно: {test}")
        else:
            print(f"Несбалансированно: {test}")