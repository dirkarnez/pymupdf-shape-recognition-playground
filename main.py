import pymupdf # imports the pymupdf library

doc = pymupdf.open("./tests/10064689564_0.pdf")  # re-open PDF
page = doc[0]  # first page
list_of_drawings = page.get_drawings()  # extract its drawings

# rgb(68, 114, 196)

list_of_drawings_bluey = [draw for draw in list_of_drawings 
    if draw['fill'] != None 
    if len(draw['fill']) == 3
    if draw['fill'][2] >  draw['fill'][1] 
    if draw['fill'][2] >  draw['fill'][0] 
    if draw['fill_opacity'] == 1 
    ]
a = len(list_of_drawings)
b = len(list_of_drawings_bluey)

# b is expected to be 3

print(list_of_drawings_bluey)

#  (0.6000000238418579, 0.6000000238418579, 0.6000000238418579)

# Out[14]:
# [
# 'items': [  # draw commands are here
#   ('re', Rect(100.0, 100.0, 200.0, 200.0), 1),  # rect from above
#   ('l', Point(100.0, 200.0), Point(200.0, 100.0)),  # first line
#   ('l', Point(200.0, 200.0), Point(100.0, 100.0)),  # second line
# ],
# 'closePath': True,  # whether to connect first & last points
# 'type': 'fs',  # a fill & stroke path
# 'stroke_opacity': 1.0,  # no border opacity
# 'color': (1.0, 0.0, 0.0),  # border color
# 'width': 1.5,  # line width
# 'lineCap': (0, 0, 0),  # line end format
# 'lineJoin': 0.0,  # line join format
# 'dashes': '[] 0',  # line dashing pattern 
# 'rect': Rect(100.0, 100.0, 200.0, 200.0),  # the original rectangle
# 'seqno': 1,  # first rendering action on page
# 'even_odd': False,  # how intersecting areas are colored
# 'fill_opacity': 1.0,  # no fill opacity
# 'fill': (1.0, 1.0, 0.0),  # fill color yellow
# }]
