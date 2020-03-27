from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        items_held = len(self.storage)
        dll = self.storage

        # if nothing, add to head
        if items_held == 0:
            self.current = dll.add_to_head(item)

        # if something but < capacity
        elif items_held > 0 and items_held < self.capacity:
            # add to tail
            self.current = dll.add_to_tail(item)

        # if something and == capacity
        elif items_held == self.capacity:
            # if current.next is None:
            if self.current.next is None:
                # remove from head
                dll.remove_from_head()
                # add to head
                self.current = dll.add_to_head(item)
            
            # if current.next is not None:
            elif self.current.next is not None:
                if self.current.next.next is None:
                    dll.remove_from_tail()
                    self.current = dll.add_to_tail(item)
                else:
                    self.current.next.insert_after(item)
                    self.current.next.delete()
                    self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        while current_node is not None:
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
                current_node = current_node.next
            else:
                continue

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        # set storage at current index to item
        self.storage[self.current] = item
        # check if at the end of storage
        if self.current + 1 < len(self.storage - 1):
            self.current += 1
        # if so, set current to 0
        else:
            self.current = 0

    def get(self):
        return_list = [item for item in self.storage if item is not None]
        return return_list
