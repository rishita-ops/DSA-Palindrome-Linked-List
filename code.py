# Define class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create linked list
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(2)
ele4 = Node(1)

# Connect nodes
ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

#Palindrome Check Function
def is_palindrome(head):
    values = []
    current = head

    # Collect all values into a list
    while current:
        values.append(current.value)
        current = current.next

    # Compare list with its reverse
    return values == values[::-1]

#Test
if is_palindrome(ele1):
    print("The linked list IS a palindrome ✅")
else:
    print("The linked list is NOT a palindrome ❌")