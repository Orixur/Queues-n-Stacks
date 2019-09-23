from sys import maxsize
"""
Simple stack class using an array (list) as data holder

"""
class Stack():

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)
		# print("Item: < " + data + ", type: " + str(type(data)) +"> pushed back!")

	def pop(self):
		if self.isEmpty():
			return (-maxsize -1)
		return self.stack.pop()

	def isEmpty(self):
		return len(self.stack) == 0

	def peek(self):
		if self.isEmpty():
			return (-maxsize -1)

		return self.stack[len(self.stack)-1]

"""
Queue built by 2 inner stacks

"""
class Queue():

	s1 = Stack()
	s2 = Stack()

	def enQueue(self, data):
		# First send all data in s1 to s2 in reverse order
		while not self.s1.isEmpty():
			self.s2.push(self.s1.peek())
			self.s1.pop()

		# Push data into s1
		self.s1.push(data)

		# Get back data into s1
		while not self.s2.isEmpty():
			self.s1.push(self.s2.peek())
			self.s2.pop()

	def deQueue(self):
		if self.s1.isEmpty():
			return "The Queue is empty!!"
		aux = self.s1.peek()
		self.s1.pop()
		return aux

"""
leafStack
"""
class StackNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class LeafStack:
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if not self.root else False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print ("% d pushed to stack" % (data))

	def pop(self):
		if self.isEmpty():
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root


"""
Special stack
	- All operations must be O(1)
		- That means that operation does not go through a loop (I think)

The special stack must NOT use other data structures like arrays, list, etc

Source: https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/

"""
class SpecialStack:
	def __init__(self):
		self.s1 = LeafStack()
		self.minS = LeafStack()

	def push(self, data):
		if self.s1.isEmpty() and self.minS.isEmpty():
			self.s1.push(data)
			self.minS.push(data)
		else:
			self.s1.push(data)
			y = self.minS.pop()
			if data < y:
				self.minS.push(data)
			else:
				self.minS.push(y)

	def pop(self):
		aux = self.s1.pop()
		self.minS.pop()
		return aux

	def isEmpty(self):
		return True if self.s1.isEmpty() else False

	def peek(self):
		aux = self.s1.peek()
		return aux

	def minD(self):
		aux = self.minS.pop()
		self.minS.push(aux)
		return aux

"""
Create a double stack structure, where both stacks use the same Array to store data

Source: https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

"""
class TwoStack:
	def __init__(self, n):
		self.size = n
		self.list = [None] * n
		self.top1 = -1
		self.top2 = self.size

	def push1(self, data):
		if self.top1 < self.top2:
			self.top1 += 1
			self.list[self.top1] = data
		else:
			print("Stack overflow")
			exit(1)

	def push2(self, data):
		if self.top1 < self.top2:
			self.top2 -= 1
			self.list[self.top2] = data

	def pop1(self):
		if self.top1 >= 0:
			aux = self.list[self.top1]
			self.list[self.top1] = None
			self.top1 = self.top1 - 1
			return aux
		else:
			print("Stack Underflow")
			exit(1)

	def pop2(self):
		if self.top1 <= self.size:
			aux = self.list[self.top2]
			self.list[self.top2] = None
			self.top2 += 1
			return aux
		else:
			print("Stack Underflow")
			exit(1)

	def showList(self):
		print(self.list)

"""
Double nested leaf stack

If the Stack have N nodes and N is even, the returned value will be the first of the second part (self.mid)
The class does NOT support mid calculation when stacks are merged

Source: https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/
"""
class DLLNode:
	def __init__(self, data):
		self.prev  = None
		self.data  = None
		self.next  = None

class DoubleLeafStack:
	def __init__(self):
		self.head = None
		self.mid = None
		self.count = 0
		self.tail = None
		self.tailFlag = False

	def push(self, data):
		newNode = DLLNode(data)
		newNode.data = data
		newNode.prev = None
		newNode.next = self.head
		self.count += 1
		if self.count == 1:
			self.mid = newNode
		else:
			self.head.prev = newNode
			if (self.count % 2) != 0:
				self.mid = self.mid.prev
		
		if not self.tailFlag:
			self.tail = newNode
			self.tailFlag = True

		self.head = newNode

	def pop(self):
		if self.count == 0:
			print("The Stack is empty!!")
			return None
		else:
			aux = self.head
			# self.head.next = None
			# self.head.prev = None
			# del self.head
			
			self.head = self.head.next
			if self.head != None:
				self.head.prev = None

			self.count -= 1
			if (self.count % 2) != 0:
				self.mid = self.mid.prev

			d = aux.data
			del aux
			return d

	def isEmpty(self):
		return True if self.count == 0 else False

	def peek(self):
		if self.count == 0:
			print("The Stack is empty!!")
			return None
		else:
			return self.tail.data

	def getHead(self):
		return self.head.data

	def getMiddleNode(self):
		if self.count == 0:
			print("The Stack is empty!!")
			return None
		else:
			return self.mid

	def printStack(self, current = None, spaces = None):
		space = spaces if spaces != None else ""
		if current == None:
			if self.head.next != None:
				space += "  "
				self.printStack(current = self.head.next, spaces = space)
			print ("<< Prev: " + (str(self.head.prev.data) if self.head.prev != None else str(None)) + " || Data: " + str(self.head.data) + " || Next: " + (str(self.head.next.data) if self.head.next != None else str(None)) + " >> (HEAD)")
			# print ("<< Prev: " + (str(self.head.prev.data) if self.head.prev != None else str(None)) + " || Data: " + str(self.head.data) + " || Next: " + (str(self.head.next.data) if self.head.next != None else str(None)) + " >> (HEAD)")
		else:
			if current.next != None:
				space += "  "
				self.printStack(current = current.next, spaces = space)
			if hex(id(current)) == hex(id(self.mid)):
				print (spaces + "┍──<< Prev: " + (str(current.prev.data) if current.prev != None else str(None)) + " || Data: " + str(current.data) + " || Next: " + (str(current.next.data) if current.next != None else str(None)) + " >> (MID)")
			else:
				print (spaces + "┍──<< Prev: " + (str(current.prev.data) if current.prev != None else str(None)) + " || Data: " + str(current.data) + " || Next: " + (str(current.next.data) if current.next != None else str(None)) + " >>")
			# print ("<< Prev: " + (str(current.prev.data) if current.prev != None else str(None)) + " || Data: " + str(current.data) + " || Next: " + (str(current.next.data) if current.next != None else str(None)) + " >>")
			

"""
Implement multiple stacks with a single array as data storage
Similar to "TwoStack" class, but scalable
Is NOT prepare to handle tricky input pairs like:
	qStack = 4 and dataLength = 2
The checking for "not in use space" is delimited by None(null) values, I think I may change that...

source: https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/
"""
class kStack:
	def __init__(self, qStacks, dataLength):
		self.qStacks = qStacks
		self.data = [None] * dataLength
		self.dataLength = dataLength
		self.tops = self.initializeStacks()

	def initializeStacks(self):
		final = {}
		prev = 0
		for i in range(1,self.qStacks+1):
			limit = ((i*self.dataLength) / self.qStacks) - 1
			final[i] = {"start" : int(prev), "end" : int(limit)}
			prev = limit + 1
		return final

	def isFull(self):
		return True if not None in self.data else False

	def isEmpty(self):
		f = True
		for d in self.data:
			if d != None:
				f = False
		return f

	def push(self, data, stack):
		if self.isFull():
			print("Stack Overflow")
			return
		l = self.tops[stack]
		commit = False
		for i in range(0, len(self.data)):
			item = self.data[i]
			if item == None and i >= l["start"] and i <= l["end"]:
				self.data[i] = data
				commit = True
				break

		if not commit:
			print("StackOverflow: The stack %s is full." % str(stack))

		print(self.data)

	def pop(self, stack):
		if self.isEmpty():
			print("The stack is empty!")
			return
		aux = None
		l = self.tops[stack]
		commit = False
		for i in reversed(range(0, len(self.data))):
			item = self.data[i]
			if item != None and i >= l["start"] and i <= l["end"]:
				aux = self.data[i]
				self.data[i] = None
				commit = True
				break
		print(self.data)
		if commit == False:
			print("The operation does not commit, cause to non value for stack <" + str(stack) + ">")
		return aux

	def peek(self, stack):
		if self.isEmpty():
			print("The stack is empty!")
			return
		aux = None
		l = self.tops[stack]
		commit = False
		for i in range(0, len(self.data)):
			item = self.data[i]
			if item != None and i >= l["start"] and i <= l["end"]:
				aux = self.data[i]
				commit = True
				break
		if commit == False:
			print("The operation does not commit, cause to non value for stack <" + str(stack) + ">")
		return aux

"""
Create a mergeable stack.
The class will inherit DoubleLeafStacks objects that will be merged from the begin of the argument to the head of the current main stack
If you continue adding leafs to the main stack and print, then you will see these new values concatenateds.
If you merged stack2 into stack1 and then merged them; then, you push a value to stack2, then stack1 will NOT be updated

Following DoubleLeafStack class, the only function with O(x) > O(1) is "printStack" 

source:https://www.geeksforgeeks.org/create-mergable-stack/
"""
class MergeableStack(DoubleLeafStack):
	def __init__(self):
		DoubleLeafStack.__init__(self)
	def mergeable(self, stack):
		if type(stack) == type(self):
			self.head.prev = stack.tail
			stack.tail.next = self.head
			self.head = stack.head

"""
Create a stack with all his methods O(1).
Additionaly implement a getMin() function (O(1))
To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.
The "getMin" solution has a time complexity of O(n), where n is the number of nodes in the stack
TO make a "getMin" solution with O(1) complexity, you need to achieve the smallest value in the time you PUSh data into stack

source: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
"""
class StackMin(DoubleLeafStack):
	def __init__(self):
		DoubleLeafStack.__init__(self)

	def getMin(self, _min = None, current = None):
		if _min == None:
			_min = _min if _min != None else self.head.data
		if current == None:
			# s_min = self.head.data if _min == None else self.head.data if self.head.data < _min else _min
			if self.head.next:
				_min = self.head.data if _min == None else self.head.data if self.head.data < _min else _min
				_min = self.getMin(_min = _min, current = self.head.next)
			# else:
			# 	return _min
		else:
			if current.next:
				_min = current.data if current.data < _min else _min
				_min = self.getMin(_min = _min, current = current.next)
			else:
				_min = current.data if current.data < _min else _min
				
		return _min

if __name__ == '__main__':
	# queue = Queue()

	# queue.enQueue("3")
	# queue.enQueue("2")
	# queue.enQueue("1")

	# print(queue.deQueue())
	# print(queue.deQueue())
	# print(queue.deQueue())
	# print("---------------------------------")
	
	# #-------------------
	
	# leafStack = LeafStack()
	# for i in range(0,5):
	# 	leafStack.push(i)

	# while not leafStack.isEmpty():
	# 	print(leafStack.pop())
	
	#-------------------
	
	# specialstack = SpecialStack()
	# specialstack.push(10)
	# specialstack.push(20)
	# specialstack.push(30)
	# print(specialstack.minD())
	# specialstack.push(5)
	# print(specialstack.minD())
	
	#-------------------

	# ts = TwoStack(5)
	# ts.push1(5) 
	# ts.push2(10) 
	# ts.push2(15) 
	# ts.push1(11) 
	# ts.push2(7)
	# ts.showList()

	# print("Popped element from stack1 is " + str(ts.pop1()))
	# ts.push2(40) 
	# print("Popped element from stack2 is " + str(ts.pop2())) 
	# ts.showList()

	#-------------------

	# ds = DoubleLeafStack()
	# ds.push("a")
	# ds.push("b")
	# ds.push("c")
	# ds.printStack()
	# a = ds.pop()
	# print(a)
	# ds.printStack()

	#-------------------

	# s = kStack(qStacks = 3, dataLength = 9)
	# s.push(1, 1)
	# s.push(2, 1)
	# s.push(2, 2)
	# s.push(3, 3)
	# # print(s.pop(1))
	# # print(s.pop(1))
	# # print(s.pop(1))
	# print(s.peek(1))
	# print(s.peek(2))
	# print(s.peek(3))

	#-------------------

	# ms = MergeableStack()
	# ms.push(1)
	# ms.push(2)
	# ms.push(3)
	# # ms.printStack()
	# ms2 = MergeableStack()
	# ms2.push(4)
	# ms2.push(5)
	# ms2.push(6)
	# ms.mergeable(ms2)
	# ms.push(7)
	# ms.push(8)
	# # ms2.printStack()
	# # print()
	# # ms.printStack()
	# # ms3 = MergeableStack()
	# # ms3.push(7)
	# # ms3.push(8)
	# # ms3.push(9)
	# # ms.mergeable(ms3)
	# ms.printStack()

	#-------------------
	s = StackMin()
	s.push(18)
	s.push(19)
	s.push(29)
	s.push(15)
	s.push(16)
	s.printStack()
	print("Res:", s.getMin())
	s.pop()
	s.pop()
	s.printStack()
	print("Res:", s.getMin())

