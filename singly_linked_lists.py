class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head != None:
            current_head = self.head
            self.head = self.head.next
            return current_head
    def remove_from_back(self):
        if self.head == None:
            return None

        runner = self.head
        while (runner.next.next):
            runner = runner.next
        runner.next = None
        return runner
    
        
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

my_list.remove_from_front()

my_list.print_values()

another_one = SList()
another_one.add_to_front("Hi").add_to_back("my name is").add_to_back("Slim Shady").print_values()
another_one.remove_from_front()
another_one.print_values()

another_one.remove_from_back()


