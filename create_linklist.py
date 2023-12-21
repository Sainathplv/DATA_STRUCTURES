# initialization of a node where every node has value and pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Class of linked_list for various operations which use node function for creating a node.
# where head and tail are first value and last value of a sequence
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # append function is to add a node in the end of a sequence,
    # where for that we need to alter the tail's pointer to the new node
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # pop is to delete the node and end of a sequence so alter the tail's but one node pointer to none
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_at_index(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        a = self.get_value(index - 1)
        new_node.next = a.next
        a.next = new_node
        self.length += 1
        return True

    def pop_at_index(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        a = self.get_value(index - 1)
        b = a.next
        a.next = b.next
        b.next = None
        self.length -= 1
        return b

    # here there is a logic where temp will be head,head becomes tail and tail becomes head
    # traverse along the loop until max length where first after is temp.next and then to none
    # then switching the variables to connect the link
    def rev(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # here one variable has to jump twice and one var moves one step
    # second approach: n+1/2 or n/2 can also take pace but require other function to calculate the length
    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return

        seen = set()
        current = self.head
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next
                self.length -= 1
            else:
                seen.add(current.value)
                prev = current
            current = current.next

    def binary_to_decimal(self):
        result = 0
        current = self.head
        while current:
            result = result * 2 + current.value
            current = current.next
        return result

    def reverse_between(self, start_index, end_index):
        if self.head is None or start_index == end_index:
            return

        # Initialize pointers
        current = self.head
        prev = None

        # Move to the start position
        for _ in range(start_index):
            prev = current
            current = current.next

        # Start the reversal process
        tail = current
        new_next = None
        for _ in range(end_index - start_index + 1):
            next_node = current.next
            current.next = new_next
            new_next = current
            current = next_node

        # Reconnect the reversed part with the rest of the list
        if prev:
            prev.next = new_next
        else:
            self.head = new_next

        tail.next = current


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    # Move fast k nodes ahead
    for _ in range(k):
        if fast is None:
            return None  # k is larger than the length of the list
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


create_linked_list = LinkedList(4)
create_linked_list.append(2)
create_linked_list.prepend(9)
create_linked_list.pop_first()
create_linked_list.set_value(1, 7)
create_linked_list.insert_at_index(5, 2)
create_linked_list.insert_at_index(1, 2)
create_linked_list.print_list()
print("Above is before pop of index")
print("deleted value at the index is ", create_linked_list.pop_at_index(2).value)
create_linked_list.print_list()
print("after reverse")
create_linked_list.rev()
create_linked_list.print_list()
