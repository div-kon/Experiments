fill(.7,.9,.8)
rect(0,0,width(), height())

translate(0, 150)
scale(.9)
stroke(1, 0, 1)
fill(None)
strokeWidth(140)


strokeWidth(20)
#lineDash(30,30)
lineJoin("round")
#lineCap("round")
path = BezierPath()
#f
path.moveTo((170, 220))
path.lineTo((170, 470))
path.curveTo((120, 520), (170, 580), (240, 580))
path.curveTo((250, 580), (320, 600), (310, 470))
path.lineTo((140, 430))
path.lineTo((290, 430))
#a
path.curveTo((360, 430), (400, 420), (400, 280))
path.lineTo((400, 230))
path.lineTo((470, 240))
#path.moveTo((80, 430))
oval(251, 228,140, 130)
#r
#path.moveTo((460, 240))
path.lineTo((510, 560))
path.lineTo((420, 430))
path.lineTo((560, 430))
path.lineTo((550, 330))
path.curveTo((530, 220),(620, 230),(625, 230))
#g
path.curveTo((780, 230),(780, 350),(780, 350))
path.curveTo((780, 400),(760, 440),(709, 440))
path.curveTo((600, 440),(590, 260),(790, 177))
path.oval(581, 88,260, 99)
path.moveTo((680, 434))
path.lineTo((860, 480))
path.lineTo((830, 350))
#o
path.oval(831, 229,140, 210)
drawPath(path)
help(qCurveTo)