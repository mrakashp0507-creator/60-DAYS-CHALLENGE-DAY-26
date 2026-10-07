# Day 26 — Remove Nth Node from End

## Phase: Two Pointer Optimization

### Problem Statement

A secret communication system stores messages in a singly linked list. One corrupted message must be removed based on its position from the end.

The objective is to remove the Nth node from the end using a single traversal.

### Algorithm

The solution uses two pointers and a dummy node.

1. Initialize `slow` and `fast` at the dummy node.
2. Move `fast` forward by `n + 1` steps.
3. Advance both pointers until `fast` reaches the end.
4. The node after `slow` is the target.
5. Update `slow.next` to skip the target node.
6. Update the head and return the removed message.

### Example

Original:

`MSG-A -> MSG-B -> MSG-C -> MSG-D -> MSG-E -> None`

N = 2

Removed: `MSG-D`

Result:

`MSG-A -> MSG-B -> MSG-C -> MSG-E -> None`

### Why Two Pointers?

The gap between the pointers allows the target node to be located from the end without counting the list in a separate traversal.

### Edge Cases

* Remove the last node.
* Remove the first node.
* Remove the only node.
* Reject zero or negative N.
* Reject N greater than the list length.

### Complexity

Time: O(n)

Auxiliary space: O(1)

### How to Run

`python day26_remove_nth_from_end.py`

### Learning Outcomes

* Implemented a singly linked list.
* Applied the two-pointer technique.
* Used a dummy node to simplify edge cases.
* Removed a node by changing pointers.
* Compared single-pass and two-pass traversal.
