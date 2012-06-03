#!/usr/bin/env python 
# ============================================================================
import sys

# ======================================================
# = http://www.pythonchallenge.com/pc/def/channel.html =
# ======================================================

# ----------------------------------------------------------------------------
def findNextNothing(nothing):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  f = file("channel/%s.txt" % nothing)
  next_found = False
  while not next_found:
    contents = f.readline()
    if len(contents) == 0:
      break
    
    print contents
    next = contents.split()[-1]
    if next.isdigit(): 
      next_found = True
      print next
    else:
      print "different - - - - "
  
  print '=============='
  if not next_found:
    return None
  return next

# ----------------------------------------------------------------------------
def getAllNothings(start_nothing):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  list_of_nothings = [start_nothing]
  next_nothing = start_nothing
  for i in xrange(1000):
    next_nothing = findNextNothing(next_nothing)
    if next_nothing == None:
      break
    list_of_nothings.append(next_nothing)
  return list_of_nothings

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  start_nothing = '90052'
  list_of_nothings = getAllNothings(start_nothing)

  print "==================="
  print list_of_nothings
  
  # f = file('channel.zip')
  # for x in f.readline(): 
  #   print x
  # # x, y = zip(f.readline())
  # print '======================='
  # print x
  # print '======================='
  # print y
  # # for l in f.readline():
  # #   print '---------------'
  # #   print l

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 
