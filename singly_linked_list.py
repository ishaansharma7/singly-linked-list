class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def print_list(self):
        if self.head is None:
            print('linked list empty!!')
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next
        
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


    def delete(self,data):
        if self.head is None:
            print('linked list empty!!')
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next
    

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        curr_node = self.head
        for _ in range(position-1):
            if curr_node is None:
                print('index out of range')
                return
            curr_node = curr_node.next
        new_node.next = curr_node.next
        curr_node.next = new_node


    def delete_at_position(self, position):
        if self.head is None:
            print('linked list empty!!')
            return
        if position == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        previous = None
        for i in range(position):
            if curr_node is None:
                print('index out of range')
                return
            if curr_node.next is None:
                break
            previous = curr_node
            curr_node = curr_node.next
        
        previous.next = curr_node.next if curr_node else None
    

    def reverse(self):
        previous = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next # Save the next node before reversing the link
            curr_node.next = previous # Reverse the link

            # Move to the next nodes for the next iteration
            previous = curr_node 
            curr_node = next_node
        self.head = previous

    
    def has_cycle(self):
        if self.head is None:
            return False
        slow_ptr = self.head
        fast_ptr = self.head.next
        while fast_ptr is not None or fast_ptr.next is not None:
            if slow_ptr == fast_ptr:
                return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return False
