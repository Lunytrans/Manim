from manim import *

class M(Scene):
    def construct(self):
        map=NumberPlane(background_line_style={
            "stroke_color":RED_E,
            "stroke_width":1,
            "stroke_opacity":0.5
        })
        map.axes.set_opacity(0)
        self.add(map)
        
        cau=Text("Cauchy-Schwarz inequality",font="times new roman",font_size=70).set_color_by_gradient(PURPLE,BLUE)

        self.play(Write(cau),run_time=1)
        self.play(cau.animate.shift(UP*3.5+RIGHT*4.2).scale(0.4))


        R = 3  # bán kính đường tròn
        center = ORIGIN
        A = center + LEFT * R
        B = center + RIGHT * R
        M = center  # trung điểm AB

        semicircle = Arc(radius=R, start_angle=0, angle=PI, color=BLUE)

        theta_tracker = ValueTracker(PI / 3)
        

        def get_C():
            angle = theta_tracker.get_value()
            return center + R * np.array([np.cos(angle), np.sin(angle), 0])

        def get_triangle():
            C = get_C()
            return Polygon(A, B, C, color=WHITE,fill_color=PURPLE,fill_opacity=0.3)

        def get_moving_dot():
            return Dot(get_C(), color=RED).scale(0.7)

        def get_median():
            return Line(get_C(), M, color=ORANGE)

        def get_altitude():
            C = get_C()
            x = C[0]
            H = np.array([x, 0, 0])
            return Line(C, H, color=GREEN)

        def get_foot_of_altitude():
            C = get_C()
            x = C[0]
            return Dot([x, 0, 0], color=TEAL).scale(0.5)
        def vh():
            C=get_C()
            x=C[0]
            H = np.array([x, 0, 0])
            return RightAngle(Line(A,B),Line(C,H),length=0.2,quadrant=(-1,-1))

        # Các thành phần động
        triangle = always_redraw(get_triangle)
        moving_dot = always_redraw(get_moving_dot)
        median = always_redraw(get_median)
        altitude = always_redraw(get_altitude)
        foot_dot = always_redraw(get_foot_of_altitude)
        v_h=always_redraw(vh)
        m_1=always_redraw(lambda:MathTex("M").next_to(get_C(),UP))
        h_1=always_redraw(lambda:MathTex("H").next_to(get_foot_of_altitude(),DOWN))
        vg=VGroup(triangle,moving_dot, median, altitude, foot_dot,v_h)


        # Các điểm cố định
        dot_A = Dot(A, color=YELLOW).scale(0.6)
        dot_B = Dot(B, color=YELLOW).scale(0.6)
        dot_M = Dot(M, color=GREEN).scale(0.6)

        label_A = MathTex("A").next_to(dot_A, LEFT)
        label_B = MathTex("B").next_to(dot_B, RIGHT)
        label_O = MathTex("O").next_to(dot_M, DOWN)

        oab=MathTex(r"AH=",
                   r"a",
                   r"\\",
                   r"BH=",
                   r"b").shift(UP*2.5+LEFT*5.5).scale(0.8)
        oab[1].set_color(YELLOW)
        oab[4].set_color(YELLOW)
        
        om=MathTex(r"OM=\frac{AB}{2}")
        om1=MathTex(r"OM=",r"\frac{a+b}{2}")
        om1[1].set_color(YELLOW)
        omv=VGroup(om,om1).shift(UP*1.5).scale(0.8)

        hm=MathTex(r"HM=\sqrt{AH.BH}")
        hm1=MathTex(r"HM=",r"\sqrt{ab}")
        hm1[1].set_color(YELLOW)
        hmv=VGroup(hm,hm1).scale(0.8).shift(UP*0.4)

        voh=VGroup(om,hm,om1,hm1).next_to(oab,DOWN*2.5)
        voh1=VGroup(om,hm)
        

        # Hiển thị hình
        self.play(Create(semicircle))
        self.play(FadeIn(dot_A, dot_B, dot_M, label_A, label_B, label_O,m_1,h_1,vg),run_time=1.5)
        self.play(FadeIn(oab))
        self.play(Write(voh1))
        self.play(Transform(om,om1),
                  Transform(hm,hm1),
                  FadeOut(oab))



        # Hoạt ảnh di chuyển điểm m
        self.play(theta_tracker.animate.set_value(PI * 0.8), run_time=2, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)
        
        f1=MathTex(r"OM",
                   r">",
                   r"HM").shift(DOWN*2)
        f2=MathTex(r"\geq").shift(DOWN*2)
        f1[0].set_color(ORANGE)
        f1[2].set_color(GREEN)
        self.play(Write(f1))
        self.wait()

        self.play(FadeOut(label_O),
                  theta_tracker.animate.set_value(PI * 0.5), run_time=1, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)
        self.play(Transform(f1[1],f2))
        t1=MathTex(r"\frac{a+b}{2}",
                   r"\sqrt{ab}")
        t1[0].set_color(ORANGE).next_to(f2,LEFT)
        t1[1].set_color(GREEN).next_to(f2,RIGHT)
        self.play(Transform(f1[0],t1[0]))
        self.play(Transform(f1[2],t1[1]))
        vv=VGroup(t1[0],t1[1],f2)
        box=SurroundingRectangle(vv,color=PURPLE)
        
        self.play(Create(box),theta_tracker.animate.set_value(PI * 0.2), run_time=1, rate_func=rate_functions.ease_in_out_sine)
        self.play(theta_tracker.animate.set_value(PI*0.8),run_time=2,rate_func=rate_functions.ease_in_out_sine)
        

        
        
        self.wait()
