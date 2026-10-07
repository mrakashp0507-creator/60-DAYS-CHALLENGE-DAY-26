# Day 26 - Two Pointer Optimization
# Remove Nth Node From End of Linked List


class Node:
    def __init__(self, message):
        self.data = message
        self.next = None


class MessageChain:
    def __init__(self):
        self.head = None

    def append(self, message):
        new_node = Node(message)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print(" -> None")


def remove_nth_from_end(head, n):
    # Dummy node makes it easier to handle
    # the case where the head itself is removed.
    dummy = Node("DUMMY")
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # slow is now just before the node to remove
    if slow.next is not None:
        slow.next = slow.next.next

    return dummy.next


print("======================================")
print("     SECRET MESSAGE CHAIN")
print("======================================")

message_chain = MessageChain()

messages = [
    "MSG-A",
    "MSG-B",
    "CORRUPTED",
    "MSG-D",
    "MSG-E"
]

for message in messages:
    message_chain.append(message)

print("\nOriginal Message Chain:")
message_chain.display()

n = int(input("\nEnter n (node to remove from end): "))

if n <= 0:
    print("n must be greater than 0.")
else:
    new_head = remove_nth_from_end(message_chain.head, n)

    print("\nMessage Chain After Removal:")

    current = new_head

    while current is not None:
        print(current.data, end="")

        if current.next is not None:
            print(" -> ", end="")

        current = current.next

    print(" -> None")

    print("\nCorrupted message removed successfully!")