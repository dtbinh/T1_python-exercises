add_library('peasycam')
add_library('hd')

def setup():
    size(1200,675,P3D)
    cam = PeasyCam(this,500)
    noStroke()
    
    global dx,dy,dz
    dx = 500.0
    dy = 400.0
    dz = 300.0
    b = Box(-dx/2,-dy/2,-dz/2,dx/2,dy/2,dz/2)
    vs = VoxelSpace()
    vs.construct(b,3.0)
    vs.setValueToAll(10000)
    vd = VoxelDistance(vs)
    
    vb = VBox(-200,-150,-100,200,150,100)
    vd.addVol(vb,b)
    
    t = Torus(-200,-150,0,150,40)
    vd.subVol(t,b)
    
    c = Cylinder(-100,250,0,-120,0,0,30)
    vd.subVol(c,b)
    
    bx = VBox(80,100,-50, 180,200,50, 20)
    vd.subVol(bx,b)
    
    vs.makeShell(10,1)
    
    for i in range(60):
        x = random(-160,160)
        y = random(-120,120)
        v = PVector.random2D()
        v.mult(random(0,20))
        xt = x + v.x
        yt = y + v.y
        cl = Cylinder(x,y,-90,xt,yt,90,5)
        vd.addSmooth(cl,b,30)
        
    vd.subVol(t,b)
    vd.subVol(c,b)
    vd.subVol(bx,b)
    vd.intVol(vb,b)
    
    cut = VBox(-dx/2,-dy/2,20,dx/2,dy/2,dz/2)
    vd.subVol(cut,b)
    
    global shp
    shp = vs.getPShape(this,0.0)
    
def draw():
    background(77)
    directionalLight(255,127,  0, 1, 0, 0)
    directionalLight(  0,255,127, 0, 1, 0)
    directionalLight(127,  0,255, 0, 0, 1)
    directionalLight(255,  0,127,-1, 0, 0)
    directionalLight(127,255,  0, 0,-1, 0)
    directionalLight(  0,127,255, 0, 0,-1)
    
    shape(shp)
    
    global dx,dy,dz
    noFill()
    stroke(255)
    box(dx,dy,dz)
    box(5)
    
    
    
    
    
    
    
    
    
    