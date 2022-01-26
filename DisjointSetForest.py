class DisjointSetForest:
  def __init__(self, n):
    self.forest = [-1] * n
    self.total = 0

  # Problem 6 # Problem 7
  def find(self, a):
    if a < 0 or a >= len(self.forest):
      raise Exception("Out of bounds")
      return -1

    if self.forest[a] < 0:
      return a

    return self.find(self.forest[a])