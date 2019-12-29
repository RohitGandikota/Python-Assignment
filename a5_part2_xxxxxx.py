class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    
class Rectangle(Point):
    'class that represents a rectangle in the plane'

    def __init__(self, p1, p2, color):
        ''' (Rectangle,Point, Point, str) -> None
        initialize rectangle with bottom left cordinate as p1 and top right as p2'''
        self.p1 = p1
        self.p2 = p2
        self.color = color
        
    def get_bottom_left(self):
        """ 
        (Rectangle) -> list
        Returns the bottom left co-ordinates 
        
        """
        return self.p1.get() # assuming that first point is always bottom left (as given in assignment)
    
    def get_top_right(self):
        """
        (Rectangle) -> list
        Returns the top right co-ordinates 
        """
        return self.p2.get()
    
    def get_color(self):
        """ 
        (Rectangle)- > str
        Returns the color of the rectangle 
        """
        return self.color
    
    def reset_color(self, color_new):
        """ changes the color of the rectangle """
        self.color = color_new
        
    def get_perimeter(self):
        """ 
        (Rectangle) -> float
        get perimeter of the rectangle 
        
        Returns perimeter of the rectangle
        """
        diffx = abs(self.p1.x - self.p2.x)
        diffy = abs(self.p1.y - self.p2.y)
        perimeter = 2*(diffx+ diffy)
        return perimeter
    
    def get_area(self):
        """ 
        (Rectangle) -> float
        Get the area of the area of the rectangle 
        
        Returns area of rectangle
        """
        diffx = abs(self.p1.x - self.p2.x)
        diffy = abs(self.p1.y - self.p2.y)
        area = diffx*diffy
        return area
    
    def move(self, dx,dy):
        """ Moves the rectangle by dx in x direction and dy in y direction """
        self.p1 = self.p1.move(dx,dy)
        self.p2 = self.p2.move(dx,dy)
        
    def intersects(self, rect1):
        """
        (Rectangle, Rectangle) -> bool
        checks for intersection of the rectangle with other rectangle rect1 
        
        Returns True if intersects else False 
        """
        if(self.p1.x > rect1.p2.x or rect1.p1.x > self.p2.x): 
            return False
    
        if(self.p1.y > rect1.p2.y or rect1.p1.y > self.p2.y): 
            return False
  
        return True        
    
    def contains(self, x , y):
        """ 
        (Rectangle, float, float) -> bool
        Checks for point (x,y) lying in rectangle 
        
        Returns True if contains else False
        """
        if(self.p1.x > x or self.p2.x < x): 
            return False
    
   
        if(self.p1.y > y or self.p2.y < y): 
            return False
  
        return True
    
    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same points'''
        return self.p1.x == other.p1.x and self.p1.y == other.p1.y and self.p2.x == other.p2.x and self.p2.y == other.p2.y
    
    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(Point1, Point2, color) '''
        return 'Rectangle(Point('+str(self.p1.x)+','+str(self.p1.y)+'), Point('+str(self.p2.x)+','+str(self.p2.y)+'),\''+ self.color+'\')'
    
    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Rectangle(Point1, Point2, color).
        In this case we chose the same representation as in __repr__'''
        return 'I am a '+self.color+' rectangle with bottom left corner at '+ '('+str(self.p1.x)+','+str(self.p1.y)+') '+'and top right corner at '+'('+str(self.p2.x)+','+str(self.p2.y)+')'+'.'


class Canvas():
    def __init__(self):
        """
        Initial an empty canvas
        """
        self.canvas = []
        
    def add_one_rectangle(self,Rectangle):
        """
        (Canvas, Reactangle) -> void
        
        Adds a rectangle to the canvas
        """
        self.canvas.append(Rectangle)
    def count_same_color(self,color):
        """
        (Canvas, str) -> int
        
        Counts the number of rectangles with the same color as specified
        Returns the number of same colored rectangles in the canvas
        """
        cnt =0
        for r in self.canvas:
            if r.color == color:
                cnt += 1
        return cnt
    def total_perimeter(self):
        """
        (Canvas) -> float
        Returns the sum of perimeters of all the existing rectangles
        """
        total_perimeter = 0
        for r in self.canvas:
            total_perimeter = total_perimeter + r.get_perimeter()
        return total_perimeter
    def min_enclosing_rectangle(self):
        """
        (Canvas) -> Rectangle
        Returns the rectangle that bounds the canvas 
        """
        x_min = 1000000
        y_min = 1000000
        
        x_max = -1000000
        y_max = -1000000
        for r in self.canvas:
            if r.p1.x < x_min:
                x_min = r.p1.x
            if r.p2.x > x_max:
                x_max = r.p2.x
                
            if r.p1.y < y_min:
                y_min = r.p1.y
            if r.p2.y > y_max:
                y_max = r.p2.y
        return Rectangle(Point(x_min,y_min), Point(x_max,y_max), 'red')
    
    def common_point(self):
        """
        (Canvas)  -> bool
        Checks if all the rectangles have atleast a single common point
        """
        for i in range(len(self.canvas)):
            for j in range(len(self.canvas)):
                if self.canvas[i].intersects(self.canvas[j]):
                    pass
                else:
                    return False
        return True
                
                
    def __len__(self):
        """
        (Canvas) -> str
        Returns the length of Canvas
        """
        return len(self.canvas)
    
    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation Canvas(Rectangle(Point1, Point2, color), .....) '''
        string = "Canvas([" 
        for r in self.canvas:
            string = string + repr(r) + ' ,'
        string = string[:-1] + '])'
        return string                           
            
        