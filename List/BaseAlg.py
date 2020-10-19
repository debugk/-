
#==============================================================================
# 反转链表
#==============================================================================
def invert_list(head):
    pre_node = None
    cur_node = head

    while cur_node:
        helper = cur_node.next
        cur_node.next = pre_node # point to previous node
        pre_node = cur_node # update the previous node to the current one
        cur_node = helper # move to next one
    
    return pre_node # return current head


#==============================================================================


