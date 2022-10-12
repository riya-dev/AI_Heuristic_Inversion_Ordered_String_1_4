# Name: Riya Dev
# Date: 10/11/2020
import random, time, math

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self
      
   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue)-1)

   # helper method for push      
   def heapUp(self, k):
      while k > 1: # ALL GOOD
         parent = k // 2
         # print("parent", self.queue[parent], "k", self.queue[k])
         if (self.queue[parent] < self.queue[k]): # if current larger than parent, swap
            return
         self.swap(parent, k)
         k = parent
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2 * k, 2 * k + 1

      if left == size and self.queue[k] > self.queue[size]: # last case
         self.swap(k, size)
      
      elif right <= size:
         min = (left if self.queue[left] <= self.queue[right] else right)
   
         if self.queue[k] > self.queue[min]:
            self.swap(k, min)
            self.heapDown(min, size)
   
   # make the queue as a min-heap            
   def reheap(self):
      for x in range(len(self.queue)//2, 0, -1):
         self.heapDown(x, size)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      self.swap(1, len(self.queue)-1)
      pop = self.queue.pop()
      self.heapDown(1, len(self.queue)-1)
      return pop
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      self.swap(index + 1, len(self.queue)-1) #swap with last index, index + 1 because of dummy
      pop = self.queue.pop()
      self.heapDown(index + 1, len(self.queue)-1)
      return pop

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   """
   # Your code goes here
   numInversions = 0
   for i in range(0, N * N):
      for j in range (0, N * N):
         if i < j and new_state[i] > new_state[j]:
             numInversions += 1
   # print("numInversions-", numInversions)
            
   if N % 2 == 1:
      if numInversions % 2 == 0:
         return True
   elif N % 2 == 0:
      if 0 <= new_state.find("_") <= 3 or 8 <= new_state.find("_") <= 11:
         if numInversions % 2 == 0:
            return True
      else:
         if numInversions % 2 == 1:
            return True

   return False
   """
   numInversions = 0
   numInversionList = []
   for i in range(0, N * N):
      for j in range (0, N * N):
         if i < j and new_state[i] > new_state[j]:
            if not(new_state[j].isnumeric() and not new_state[i].isnumeric()):
               if not new_state[i] == "_":
                  if not new_state[i].isnumeric() and new_state[j].isnumeric():
                        numInversions += 1
                        numInversionList.append(new_state[i] + new_state[j])
                  else:
                     numInversions += 1
                     numInversionList.append(new_state[i] + new_state[j])

   # print("numInversions-", numInversions)
   print(numInversions, numInversionList)
            
   if N % 2 == 1:
      if numInversions % 2 == 0:
         return True
   elif N % 2 == 0:
      if 0 <= new_state.find("_") <= 3 or 8 <= new_state.find("_") <= 11:
         if numInversions % 2 == 0:
            return True
      else:
         if numInversions % 2 == 1:
            return True
      """
      0 1 2 3
      4 5 6 7
      8 9 10 11
      12 13 14 15
      """
   return False

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   # print(t1, t2, f1, f2)
   
   return t1 and t2 and not (f1 or f2)

def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   return n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:] # rturn up to i, j, the char from i+1 to just before j, i, then the rest from j+1
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   blank = state.find('_')
   '''your code goes here'''
   up, down, left, right = blank - size, blank + size, blank - 1, blank + 1
   if down < len(state): children.append(swap(state, blank, down))
   if right % size != 0: children.append(swap(state, blank, right))
   if up > -1: children.append(swap(state, up, blank))
   if left % size != (size - 1): children.append(swap(state, left, blank))
   return children
   
def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   count = 0
   for i in range(0, len(state)):
      if state[i] != goal[i]: count += 1
   return count

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic = dist_heuristic, size = 4):
   frontier = HeapPriorityQueue()
   h = heuristic(start)
   explored = {}
   explored[start] = h
   frontier.push((h, start, [start]))
   
   while not frontier.isEmpty():
      p = frontier.pop()
      if p[1] == goal:
         return p[2]
      for a in generate_children(p[1]):
         g = len(p[2]) + 1
         h = heuristic(a)
         if a not in explored or explored[a] > h + g:
            frontier.push((h + g, a, p[2]+[a]))
            explored[a] = h + g
   return None   

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()

''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''