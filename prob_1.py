#!/usr/bin/env python 
# ============================================================================

# ==================================================
# = http://www.pythonchallenge.com/pc/def/map.html =
# ==================================================

# in_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
in_string = "map"
out_string = ''

# ----------------------------------------------------------------------------
def trans(in_char):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  skip_char = ['.', ' ', '\'']
  out_char = in_char
  if not out_char in skip_char:
    out_char = chr(ord(ch)+2)
    if out_char > 'z':
      out_char = chr(ord(ch)-24)
  return out_char

# ----------------------------------------------------------------------------
for ch in in_string:
  out_string += trans(ch)
print out_string

# ============================================================================
# ============
# = solution =
# ============
# 
