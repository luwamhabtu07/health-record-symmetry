class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def isHealthRecordSymmetric(head):
    if not head or not head.next:
        return True  # empty or single node is symmetric

    # Find middle of the list
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half_start = reverse_list(slow.next)

    # Compare both halves
    p1 = head
    p2 = second_half_start
    result = True
    while p2:
        if p1.value != p2.value:
            result = False
            break
        p1 = p1.next
        p2 = p2.next

    # (Optional) Restore the list
    slow.next = reverse_list(second_half_start)

    return result
