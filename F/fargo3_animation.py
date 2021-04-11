for i in range(50):
    
    fill(.7,.9,.8)
    rect(0,0,width(), height())

    translate(0, 180)
    scale(.9)
    stroke(1, 0, 1)
    fill(None)
    strokeWidth(140)

    strokeWidth(20)
    lineDash(10*i,30)
    lineJoin("round")
    lineCap("round")
    path = BezierPath()
    #f
    path.moveTo((150, 220))
    path.lineTo((150, 500))
    path.curveTo((150, 580), (190, 600), (220, 600))
    path.curveTo((230, 600), (290, 600), (270, 480))
    path.moveTo((80, 430))
    path.lineTo((290, 430))
    #a
    path.curveTo((360, 430), (400, 420), (400, 280))
    path.lineTo((400, 230))
    path.lineTo((490, 240))
    #path.moveTo((80, 430))
    oval(251, 228,140, 130)
    #r
    #path.moveTo((497, 240))
    path.lineTo((420, 520))
    path.lineTo((443, 430))
    path.lineTo((560, 430))
    path.lineTo((550, 330))
    path.curveTo((530, 220),(620, 230),(625, 230))
    #g
    path.curveTo((780, 230),(780, 350),(780, 350))
    path.curveTo((780, 400),(760, 440),(709, 440))
    path.curveTo((600, 440),(590, 260),(750, 187))
    path.oval(581, 58,260, 130)
    path.moveTo((830, 340))
    path.curveTo((830, 440), (810, 510), (700, 510))
    path.lineTo((700, 440))
    #path.curveTo((620, 540), (600, 520), (920, 440))
    #o
    path.oval(831, 229,160, 210)
    drawPath(path)
    
    if i<50:
        newPage()

for i in range(50):
    
    fill(.7,.9,.8)
    rect(0,0,width(), height())

    translate(0, 180)
    scale(.9)
    stroke(1, 0, 1)
    fill(None)
    strokeWidth(140)

    strokeWidth(20)
    lineDash(500-(10*i),30)
    lineJoin("round")
    lineCap("round")
    path = BezierPath()
    #f
    path.moveTo((150, 220))
    path.lineTo((150, 500))
    path.curveTo((150, 580), (190, 600), (220, 600))
    path.curveTo((230, 600), (290, 600), (270, 480))
    path.moveTo((80, 430))
    path.lineTo((290, 430))
    #a
    path.curveTo((360, 430), (400, 420), (400, 280))
    path.lineTo((400, 230))
    path.lineTo((490, 240))
    #path.moveTo((80, 430))
    oval(251, 228,140, 130)
    #r
    #path.moveTo((497, 240))
    path.lineTo((420, 520))
    path.lineTo((443, 430))
    path.lineTo((560, 430))
    path.lineTo((550, 330))
    path.curveTo((530, 220),(620, 230),(625, 230))
    #g
    path.curveTo((780, 230),(780, 350),(780, 350))
    path.curveTo((780, 400),(760, 440),(709, 440))
    path.curveTo((600, 440),(590, 260),(750, 187))
    path.oval(581, 58,260, 130)
    path.moveTo((830, 340))
    path.curveTo((830, 440), (810, 510), (700, 510))
    path.lineTo((700, 440))
    #path.curveTo((620, 540), (600, 520), (920, 440))
    #o
    path.oval(831, 229,160, 210)
    drawPath(path)
    
    if i<49:
        newPage()
                
saveImage("fargo3.mp4")