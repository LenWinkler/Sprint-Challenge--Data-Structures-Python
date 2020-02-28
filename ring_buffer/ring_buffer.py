from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        items_held = len(self.storage)
        dll = self.storage
        current = self.current

        # if nothing, add to head
        if items_held == 0:
            dll.add_to_head(item)
            current = item

        # if something but < capacity
        elif items_held > 0 and items_held < self.capacity:
            # add to tail
            dll.add_to_tail(item)
            current = item

        # if something and == capacity
        elif items_held == self.capacity
            # if current.prev is None:
                # remove from head
                # add to head
            # if current.next is None:
                # remove from tail
                # add to tail
            # if current.next is not None:

        if self.current < self.capacity:
            self.storage.add_to_head(item)
            self.current = item
        else:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        while current_node is not None:
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
            else:
                continue

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
