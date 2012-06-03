#!/usr/bin/env python 
# ============================================================================
import urllib
import sys

# ========================================================
# = http://www.pythonchallenge.com/pc/def/linkedlist.php =
# ========================================================

# ----------------------------------------------------------------------------
def findNextNothing(url):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  page = urllib.urlopen(url)
  next_found = False
  while not next_found:
    contents = page.readline()
    print contents
    next = contents.split()[-1]
    if next.isdigit(): 
      next_found = True
      print next
  print '=============='
  return next

# ----------------------------------------------------------------------------
def getAllNothings(start_url):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  next_url = start_url
  for i in xrange(400):
    next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % findNextNothing(next_url)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # start_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
  start_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
  getAllNothings(start_url)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# peak.html
