class LinkedListNode:
  def __init__(self, item=None, next=None):
    self.item = item
    self.next = next

class LinkedList:
  def __init__(self):
    self.clear()

  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0

  def is_empty(self):
    return self.size == 0

  def append(self, item):

    new_node = LinkedListNode(item=item)

    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1

  def prepend(self, item):

    self.head = LinkedListNode(item=item, next=self.head)

    if self.is_empty():
      self.tail = self.head        

    self.size += 1        

  def insert(self, idx, item):
    if idx < 0 or idx > self.size:
      raise Exception("Cannot insert -Index out of bounds")
    elif idx == 0:
      self.prepend(item=item)
    elif idx == self.size:
      self.append(item=item)
    else:
      new_node = LinkedListNode(item=item)

      temp = self.head
      for _ in range(idx - 1):
        temp = temp.next

      new_node.next = temp.next
      temp.next = new_node

      self.size += 1

  def remove_first(self):
    if self.is_empty():
      raise Exception("Cannot remove - list is empty")
    elif self.size == 1:
      self.clear()
    else:
      self.head = self.head.next
      self.size -= 1

  def remove_last(self):
    if self.is_empty():
      raise Exception("Cannot remove - list is empty")
    elif self.size == 1:
      self.clear()
    else:
      temp = self.head

      while temp.next.next:
        temp = temp.next

      temp.next = None
      self.tail = temp
      self.size -= 1

  def remove(self, idx):
    if self.is_empty():
      raise Exception("Cannot remove - list is empty")
    elif idx < 0 or idx >= self.size:
      raise Exception("Cannot remove - Index out of bounds")
    elif idx == 0:
      self.remove_first()
    elif idx == self.size - 1:
      self.remove_last()
    else:
      temp = self.head

      for _ in range(idx - 1):
        temp = temp.next

      temp.next = temp.next.next

      self.size -= 1


  def get(self, idx):
    if idx < 0 or idx >= self.size:
      raise Exception("Cannot retrieve - Index out of bounds")
    elif idx == 0:
      return self.head.item
    elif idx == self.size - 1:
      return self.tail.item
    else:
      temp = self.head

      for _ in range(idx):
        temp = temp.next

      return temp.item


  def __str__(self):
    out_lst = []
    temp = self.head

    while temp:
      out_lst.append(str(temp.item))
      out_lst.append(' ')
      temp = temp.next

    return ''.join(out_lst)

  def find(self, key):
    temp = self.head
    while temp.next != None:
      if temp.item == key:
        return temp
      else:
        temp = temp.next

    return -1

  def main():
    test_list = LinkedList()

    for i in range(4):
      test_list.append(i)
      
    print(test_list)