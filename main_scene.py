# from manim import (BLUE, BLUE_E, BOLD, DOWN, LEFT, RED, RIGHT, UP, Arrow,
#                   Create, FocusOn, Scene, Tex, Transform, Triangle, VGroup,
#                   Write)

from math import cos, log, sqrt

from manim import *


class TruIntro(Scene):
    def construct(self):
        tx_saludo = Text("Hola...").scale(2)
        tx_saludo.generate_target()
        tx_saludo.target.to_edge(UP, buff=1.0)
        self.play(Write(tx_saludo))
        self.play(MoveToTarget(tx_saludo))
        self.wait(20)


class Intro(Scene):
    def construct(self):
        # ss
        tx_que_funcion = Tex("¿Qué es una función?").scale(1.4)
        self.play(Write(tx_que_funcion))

        tx_que_funcion.generate_target()
        tx_que_funcion.target.to_edge(UP)
        tx_expl_funcion = (
            Tex(
                "Una función es un bloque de código ejecuta una serie de"
                " instrucciones."
            )
            .scale(0.8)
            .next_to(tx_que_funcion.target, DOWN, buff=0.5)
        )
        self.play(MoveToTarget(tx_que_funcion))
        self.play(Write(tx_expl_funcion), run_time=3)
        self.wait(5)

        # podemos tener la funcion trianguloPorCuadrado

        gm_arr_0 = Arrow().scale(2).next_to(tx_que_funcion, DOWN, buff=2)
        gm_tr_0 = Triangle(color=PURPLE).scale(1.2).next_to(gm_arr_0, LEFT, buff=0.5)
        tx_fn_tpc = (
            Text("transformarACuadrado")
            .scale(0.7)
            .next_to(tx_expl_funcion, DOWN, buff=0.1)
        )

        tx_fn_tpc_p = (
            Text("transformarACuadrado()", t2c={"(": RED, ")": RED})
            .scale(0.35)
            .next_to(gm_arr_0, UP, buff=0.1)
        )

        tx_fn_tpc_ps = (
            Text(
                "transformarAcuadrado(triangulo)",
                t2c={"(": RED, ")": RED, "triangulo": BLUE},
                t2w={"triangulo": BOLD},
            )
            .scale(0.32)
            .next_to(gm_arr_0, UP, buff=0.1)
        )
        gm_sq_0 = Square(color=ORANGE).scale(0.8).next_to(gm_arr_0, RIGHT, buff=0.5)

        del_gp_0 = VGroup(tx_que_funcion, tx_expl_funcion)
        self.play(FadeOut(del_gp_0, run_time=0.5))

        self.play(Create(tx_fn_tpc), run_time=1.7)

        wv = 11
        self.play(
            ApplyWave(
                tx_fn_tpc,
                ripples=wv,
                time_width=wv * 0.7,
                run_time=wv + 3,
                rate_func=linear,
            )
        )
        self.wait(1)
        self.play(Transform(tx_fn_tpc, tx_fn_tpc_p))
        self.wait(3)
        self.play(FocusOn(tx_fn_tpc_p[-2:]))
        self.wait(1)
        self.play(Write(gm_arr_0))
        self.play(Create(gm_tr_0))
        self.wait(2)
        self.play(
            Indicate(tx_fn_tpc, scale_factor=1.2, run_time=1),
        )

        gm_tr_0.save_state()

        self.play(Transform(gm_tr_0, gm_sq_0), run_time=1.5)
        self.wait(1)
        self.play(Restore(gm_tr_0), run_time=1.5)

        tx_in = (
            Text("input", slant=ITALIC, color=PURPLE)
            .scale(0.7)
            .next_to(gm_tr_0, UP, buff=0.5)
        )
        tx_out = (
            Text("output", slant=ITALIC, color=ORANGE)
            .scale(0.7)
            .next_to(gm_sq_0, UP, buff=0.5)
        )
        self.play(Indicate(gm_tr_0))
        self.play(Write(tx_in))
        self.wait(2.3)
        self.play(Transform(gm_tr_0, gm_sq_0), run_time=1.5)
        self.play(Indicate(gm_sq_0))
        self.play(Write(tx_out))
        self.wait(2.3)

        self.play(tx_out.animate.set_opacity(0.7), tx_in.animate.set_opacity(0.7))

        # rs
        self.play(Restore(gm_tr_0), FadeOut(gm_sq_0), run_time=1)
        self.wait(1)

        tr_gb_0 = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_0, LEFT, buff=0.5)

        tx_fn_con_params = (
            Text("Con parámetros", color=BLUE_E)
            .scale(0.8)
            .move_to(tx_expl_funcion.get_center())
        )
        gp_funcion = VGroup(gm_arr_0, tr_gb_0, tx_fn_tpc_ps, gm_sq_0)
        box_params = SurroundingRectangle(gp_funcion, color=BLUE_E, buff=0.2)
        self.play(
            FadeOut(tx_fn_tpc),
            FadeOut(tx_fn_tpc_p, run_time=0.2),
            Write(box_params),
            Create(tx_fn_con_params),
        )
        self.wait(4.5)
        gm_arr_param = CurvedArrow(
            tx_fn_con_params[-10:].get_center(),
            tx_fn_tpc_ps[-6:].get_center(),
            radius=10,
            color=BLUE_C,
        ).scale(0.7)

        self.play(
            Wiggle(gm_tr_0), Create(gm_arr_param), Write(tx_fn_tpc_ps), run_time=0.8
        )
        self.wait(0.5)
        self.play(
            Indicate(tx_fn_tpc_ps, scale_factor=1.7, run_time=0.8),
        )
        self.wait(0.5)
        self.play(TransformFromCopy(gm_tr_0, gm_sq_0))

        tx_fn_sin_params = (
            Text("Sin parámetros", color=GREEN_E)
            .scale(0.8)
            .next_to(gm_arr_0, DOWN, buff=1.2)
        )
        gm_arr_1 = Arrow().scale(2).next_to(tx_fn_sin_params, DOWN, buff=1)
        tx_fn_sU = (
            Text("dameUno()", t2c={"(": RED, ")": RED})
            .scale(0.4)
            .next_to(gm_arr_1, UP, buff=0.1)
        )
        tx_uno = Text("1", color=ORANGE).move_to(gm_arr_1.get_center())
        tx_uno.generate_target()
        tx_uno.target.next_to(gm_arr_1, RIGHT, buff=1)

        tr_gb = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_1, LEFT, buff=0.5)

        gm_sq_1 = Square(color=BLACK).scale(0.8).next_to(gm_arr_1, RIGHT, buff=0.5)
        gp_funcion_sin_params = VGroup(
            gm_sq_1, tr_gb, gm_arr_1, tx_fn_sU, tx_uno.target
        )
        box_sin_params = SurroundingRectangle(gp_funcion_sin_params, color=GREEN_E)

        self.play(Write(tx_fn_sin_params), Write(box_sin_params))
        self.play(Create(gm_arr_1), Create(tx_fn_sU))
        self.play(Write(tx_uno))
        self.play(MoveToTarget(tx_uno))
        # ss

        self.play(
            FadeOut(gp_funcion_sin_params),
            FadeOut(gp_funcion),
            FadeOut(box_params),
            FadeOut(box_sin_params),
            FadeOut(tx_fn_sin_params),
            FadeOut(tx_fn_con_params),
            FadeOut(gm_arr_param),
            run_time=0.7,
        )
        self.clear()
        self.wait(4)


class MasEjemplosFunciones(Scene):
    def construct(self):
        tx_title = (
            Tex(
                "Más funciones con parámetros",
            )
            .scale(1.4)
            .to_corner(UP)
        )

        self.play(Write(tx_title))
        tx_fn_suma = Text(
            "sumaDosNumeros(x, y)",
            t2c={"x": BLUE, "y": RED},
            t2w={"x": BOLD, "y": BOLD},
            font_size=20,
        ).next_to(tx_title, DOWN, buff=1)
        listing = Code(
            "sumaDosNumeros.js",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="Javascript",
        )
        box_fn = SurroundingRectangle(tx_fn_suma, color=YELLOW_E, buff=0.3)
        listing.next_to(box_fn, DOWN, buff=1)
        self.play(Write(tx_fn_suma), Write(box_fn))
        self.wait(10)
        self.play(Create(listing), run_time=1)
        self.wait(10)
        gm_arr_0 = (
            Arrow(color=BLUE).scale(0.7).next_to(box_fn.get_corner(UL), LEFT, buff=0.3)
        )
        gm_arr_1 = (
            Arrow(color=RED).scale(0.7).next_to(box_fn.get_corner(DL), LEFT, buff=0.3)
        )
        tx_x = Tex("4", color=BLUE).next_to(gm_arr_0, LEFT, buff=0.5)
        tx_y = Tex("5", color=RED).next_to(gm_arr_1, LEFT, buff=0.5)

        self.play(Create(gm_arr_0), Create(gm_arr_1))

        self.play(Write(tx_x), Write(tx_y))

        tx_op_fn = Text(
            "4 + 5 = 9", t2c={"4": BLUE, "5": RED, "9": ORANGE}, font_size=25
        ).move_to(tx_fn_suma.get_center())
        gp_nums = VGroup(tx_x, tx_y)
        copy_nums = gp_nums.copy()
        self.play(
            Create(copy_nums, run_time=0.1),
            FadeOut(tx_fn_suma),
            Transform(gp_nums, tx_op_fn),
            run_time=1.5,
        )
        self.wait(1.0)
        gm_arr_2 = Arrow(color=ORANGE).scale(0.7).next_to(box_fn, RIGHT, buff=0.3)
        tx_res_fn = Text("9", color=YELLOW_E).next_to(gm_arr_2, RIGHT, buff=0.5)
        self.play(
            FadeOut(gp_nums),
            Transform(tx_op_fn, tx_res_fn),
            FadeIn(tx_fn_suma),
            Write(gm_arr_2),
            run_time=2,
        )

        self.wait(3)


def mv_dot(dot: Dot, og_line: Line, vlt: ValueTracker):
    start = og_line.get_start()[0]
    end = og_line.get_end()[0]
    vl = vlt.get_value()
    if start <= vl <= end:
        dot.set_x(vlt.get_value())


def hp_set_opacity(obj: VMobject, og_line: Line, vlt: ValueTracker):
    vl = vlt.get_value()
    start = og_line.get_start()[0]
    end = og_line.get_end()[0]
    if start < vl > end:
        obj.set_opacity(0.2)
    #        obj.set_stroke(width=2)
    else:
        obj.set_opacity(1)


#        obj.set_stroke(width=6)


class DetallesScope(Scene):
    def construct(self):
        # ss
        tx_title = Text(
            "¿Qué es el scope(o alcance)?", t2w={"scope": BOLD}, t2c={"scope": BLUE}
        )
        self.play(Write(tx_title))
        self.play(Unwrite(tx_title), run_time=0.3)

        tx_def = Tex(
            r"{0.5\textwidth}El scope determina que partes del programa "
            r"pueden ser usadas, cuando podemos definir, redefinir y "
            r"usar una variable sin conflictos",
            tex_environment="minipage",
        )
        self.play(Write(tx_def))

        tx_brackets = Text("Se pude delimitar con {} o indentando...").to_edge(
            UP, buff=0.7
        )

        # ss
        self.play(Write(tx_brackets))

        cb_js = (
            Code(
                "scope.js",
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                style=Code.styles_list[15],
                language="Javascript",
            )
            .scale(0.5)
            .next_to(tx_brackets, DOWN, buff=1)
            .shift(LEFT)
        )

        cb_py = (
            Code(
                "pyex.py",
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                style=Code.styles_list[15],
                language="Python",
            )
            .scale(0.5)
            .next_to(cb_js, RIGHT, buff=1)
        )
        # rs

        self.play(Write(cb_js), Write(cb_py))

        self.wait(2)


class Scope(Scene):
    def construct(self):
        nm = NumberPlane().add_coordinates()
        # self.add(nm)

        color_palette = [BLUE, RED, PURPLE, YELLOW_E, ORANGE]
        lines_texts = ["Program", "main()", "if", "var_y", "for"]

        gm_ln_ogs = []
        # Initial guide-lines
        gm_ln_ogs.append(Line(start=[-6, 3.7, 0], end=[6, 3.7, 0], stroke_width=7))
        gm_ln_ogs.append(Line(start=[-5.7, 3, 0], end=[5.7, 3, 0], stroke_width=7))
        gm_ln_ogs.append(Line(start=[-5.0, 2.3, 0], end=[-0.2, 2.3, 0], stroke_width=7))
        gm_ln_ogs.append(Line(start=[0.1, 2.3, 0], end=[5.7, 2.3, 0], stroke_width=7))
        gm_ln_ogs.append(Line(start=[3, 1.6, 0], end=[4.5, 1.6, 0], stroke_width=7))

        # Dots to begining of guide-lines
        gm_dots = [
            Dot(gm_ln_ogs[i].get_start(), color=color_palette[i]).scale(1.3)
            for i in range(len(color_palette))
        ]

        # Color line redraw
        gm_ln_colored = [
            always_redraw(
                lambda i=i: Line(
                    start=gm_ln_ogs[i].get_start(),
                    end=gm_dots[i].get_center(),
                    color=color_palette[i],
                    stroke_width=7,
                )
            )
            for i in range(len(color_palette))
        ]

        gm_ln_cb = []
        gm_ln_cb.append(
            Line(start=[-6.4, 2.0, 0], end=[-6.4, -3.0, 0], color=BLUE, stroke_width=4)
        )
        gm_ln_cb.append(
            Line(start=[-6.2, 1.8, 0], end=[-6.2, -2.85, 0], color=RED, stroke_width=4)
        )
        gm_ln_cb.append(
            Line(
                start=[-6.0, 1.4, 0], end=[-6.0, -0.1, 0], color=PURPLE, stroke_width=4
            )
        )
        gm_ln_cb.append(
            Line(
                start=[-6.0, -0.3, 0],
                end=[-6.0, -2.85, 0],
                color=YELLOW_E,
                stroke_width=4,
            )
        )
        gm_ln_cb.append(
            Line(
                start=[-5.8, -1.6, 0], end=[-5.8, -2.6, 0], color=ORANGE, stroke_width=4
            )
        )

        gm_ln_ini_color_lines = [
            Line(
                start=[-6, 1, 0],
                end=[-6, -2, 0],
                stroke_width=10,
                color=color_palette[i],
            ).scale(1.5)
            for i in range(len(color_palette))
        ]
        tx_program_parts = [
            Text(
                lines_texts[i], color=color_palette[i], slant=ITALIC, font_size=20
            ).next_to(gm_ln_ini_color_lines[i], RIGHT, buff=0.2)
            for i in range(len(lines_texts))
        ]

        codeB_scope = (
            Code(
                "scope.js",
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                style=Code.styles_list[15],
                language="Javascript",
            )
            .scale(0.7)
            .to_edge(LEFT, buff=0.6)
            .shift(DOWN * 0.5)
            .scale(1.1)
        )
        displace = ORIGIN - codeB_scope.get_center() + DOWN * 1.3

        codeB_scope.shift(displace)
        for ln in gm_ln_cb:
            ln.scale(1.1).shift(displace)

        self.add(codeB_scope)

        self.play(*[Write(og_line) for og_line in gm_ln_ogs])
        self.play(*[Write(dot) for dot in gm_dots])
        self.add(*gm_ln_colored)

        for i in range(len(gm_ln_cb)):
            self.play(Create(tx_program_parts[i]), Create(gm_ln_ini_color_lines[i]))
            tx_program_parts[i].generate_target()
            tx_program_parts[i].target.next_to(gm_dots[i], DOWN, buff=0.1)
            self.play(
                MoveToTarget(tx_program_parts[i]),
                ReplacementTransform(gm_ln_ini_color_lines[i], gm_ln_cb[i]),
            )
            self.add(gm_ln_cb[i])

        for i in range(len(tx_program_parts)):
            tx_program_parts[i].add_updater(
                lambda _, i=i: tx_program_parts[i].next_to(gm_dots[i], DOWN, buff=0.1)
            )

        self.next_section()

        vlt_program_lifetime = ValueTracker(gm_ln_ogs[0].get_start()[0] - 0.5)

        for i in range(len(gm_dots)):
            gm_dots[i].add_updater(
                lambda _, i=i: mv_dot(gm_dots[i], gm_ln_ogs[i], vlt_program_lifetime)
            )

        gm_ln_dh = always_redraw(
            lambda: DashedLine(
                start=[vlt_program_lifetime.get_value(), 5, 0],
                end=[vlt_program_lifetime.get_value(), -5, 0],
                stroke_width=10,
                dash_length=0.3,
                dashed_ratio=0.5,
                color=GREEN,
            ).set_opacity(0.7)
        )
        self.play(Write(gm_ln_dh), run_time=1)
        # set opacity
        for i in range(len(gm_dots)):
            gm_ln_cb[i].add_updater(
                lambda _, i=i: hp_set_opacity(
                    gm_ln_cb[i], gm_ln_ogs[i], vlt_program_lifetime
                )
            )

            gm_dots[i].add_updater(
                lambda _, i=i: hp_set_opacity(
                    gm_dots[i], gm_ln_ogs[i], vlt_program_lifetime
                )
            )
            gm_ln_colored[i].add_updater(
                lambda _, i=i: hp_set_opacity(
                    gm_ln_colored[i], gm_ln_ogs[i], vlt_program_lifetime
                )
            )
            tx_program_parts[i].add_updater(
                lambda _, i=i: hp_set_opacity(
                    tx_program_parts[i], gm_ln_ogs[i], vlt_program_lifetime
                )
            )
            gm_ln_ogs[i].add_updater(
                lambda _, i=i: hp_set_opacity(
                    gm_ln_ogs[i], gm_ln_ogs[i], vlt_program_lifetime
                )
            )

        self.play(
            vlt_program_lifetime.animate.set_value(10), run_time=14, rate_func=linear
        )
        self.wait(2)


class Ciclos(Scene):
    def construct(self):
        tx_title_for = Tex("Ciclos").scale(2).generate_target()
        # ss
        circ = Circle(color=RED).to_edge(DOWN, buff=1.3).shift(4 * LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start, dissipating_time=0.6, stroke_opacity=[0, 1])
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))

        self.play(Write(tx_title_for))

        self.wait(3)
        self.play(FadeIn(trace), FadeIn(rolling_circle))
        self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=3, rate_func=linear)
        self.play(rolling_circle.animate.shift(8 * LEFT), run_time=3, rate_func=linear)

        self.play(
            FadeOut(rolling_circle),
            FadeOut(trace),
        )
        self.play(
            Unwrite(tx_title_for),
        )

        tx_ejemplo = Tex("Un ejemplo...").scale(2)
        tx_ejemplo.generate_target()
        tx_ejemplo.target.scale(0.5).to_corner(UL, buff=0.8)
        self.play(Write(tx_ejemplo))
        self.wait(4)
        self.play(MoveToTarget(tx_ejemplo))

        self.wait(6)

        tx_ti_algo = Tex(
            r"""
            \underline{\textbf{Algoritmo}}
            """,
            font_size=40,
        )

        tx_fst_algo = Tex(
            r"""
            \begin{enumerate} 
                \setlength{\itemsep}{0.1cm}
                \item Definir $x = 0$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Imprimir $x$
            \end{enumerate}
            """,
            font_size=22,
        )

        head_algo_worst = r"""
            \begin{enumerate} 
                \setlength{\itemsep}{0.1cm}
                \item Definir $x = 0$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$
                \item Definir $x = 1 + x$"""

        tail_algo_worst = r"""      \item Imprimir $x$
            \end{enumerate}
            """

        definir_x_1 = r"""
                \item Definir $x = 1 + x$"""

        prev_algo = Tex(
            head_algo_worst + tail_algo_worst,
            font_size=22,
        )

        vg_algo = VGroup(tx_ti_algo, tx_fst_algo).arrange(DOWN, buff=0.3)
        vg_algo.generate_target()

        pl = NumberPlane().add_coordinates()
        # self.add(pl)

        vt_n = ValueTracker(7)

        tx_n_pasos = always_redraw(
            lambda: Text(f"# Pasos {int(vt_n.get_value())}", color=BLUE)
            .scale(0.4)
            .next_to(tx_ti_algo, UP, buff=0.1)
        )

        self.play(Write(vg_algo), run_time=4)
        self.wait(10)
        self.play(Write(tx_n_pasos))
        self.wait(15)

        vg_algo -= tx_fst_algo
        prev_algo.next_to(tx_ti_algo, DOWN, buff=0.3)

        self.play(Transform(tx_fst_algo, prev_algo))

        rn_time = [1, 0.8, 0.5, 0.5, 0.5, 0.4, 0.3, 0.1]
        wait_time = [0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.3, 0.07]
        sc = [max(min(10, x) / 10, 0.5) for x in range(20, 0, -1)]

        # ss
        self.remove(tx_fst_algo)
        for i in range(20):
            head_algo_worst += definir_x_1
            vt_n.set_value(vt_n.get_value() + 1)

            new_algo = (
                Tex(
                    head_algo_worst + tail_algo_worst,
                    font_size=22,
                )
                .scale(sc[i])
                .next_to(tx_ti_algo, DOWN, buff=0.3)
            )

            if i >= 7:
                self.play(FadeTransform(prev_algo, new_algo), run_time=rn_time[7])
                self.wait(wait_time[7])
            else:
                self.play(FadeTransform(prev_algo, new_algo), run_time=rn_time[i])
                self.wait(wait_time[i])

            self.remove(prev_algo)
            prev_algo = new_algo

        # ss
        self.play(vt_n.animate.set_value(100))

        vg_algo += prev_algo

        self.wait(5)

        self.play(FadeOut(tx_n_pasos))

        self.play(vg_algo.animate.shift(LEFT * 2))

        tx_ti_algo_mej = (
            Tex(
                r"""
            \underline{\textbf{Algoritmo Mejorado}}
            """,
                font_size=40,
            )
            .move_to(tx_ti_algo.get_center())
            .shift(RIGHT * 4)
        )
        self.play(Write(tx_ti_algo_mej))

        tx_fst_algo_mej = Tex(
            r"""
            \begin{enumerate} 
                \setlength{\itemsep}{0.1cm}
                \item Definir $x = 0$
                \item Repetir paso 3 por 100 veces 
                \item Definir $x = 1 + x$
                \item Imprimir $x$
            \end{enumerate}
            """,
            font_size=22,
        ).next_to(tx_ti_algo_mej, DOWN, buff=0.4)
        self.play(Write(tx_fst_algo_mej), run_time=7)
        self.wait(24)

        vg_algo = vg_algo + tx_ejemplo + tx_fst_algo_mej + tx_ti_algo_mej

        # rs
        self.play(FadeOut(vg_algo), run_time=1.5)

        tx_pero = Tex(r"""\textbf{Pero ¿por qué no simplemente...}  x += 100?""")

        self.play(Write(tx_pero))
        self.wait(3)
        wv = 16
        self.play(ApplyWave(tx_pero, ripples=wv, time_width=wv, run_time=wv))

        self.wait(5)


class LosCiclos(Scene):
    def construct(self):
        grid = NumberPlane().add_coordinates().set_opacity(0.3)
        # self.add(grid)
        # ss
        tx_ti_ciclos = Tex(
            r"""\textbf{Ciclos usados en programación...}""", font_size=22
        ).scale(2.7)
        tx_for_while = (
            Tex(
                R"""
                El for y el while son esencialmente lo mismo...
                """,
                tex_to_color_map={"while": GREEN, "for": BLUE},
                font_size=22,
            )
            .scale(1.7)
            .to_edge(UP, buff=0.3)
        )

        self.play(Write(tx_ti_ciclos))

        self.wait(1)

        self.play(Unwrite(tx_ti_ciclos), run_time=0.5)
        self.play(FadeTransform(tx_ti_ciclos, tx_for_while))
        self.wait(3)

        gm_circle = (
            Circle(radius=sqrt(2), stroke_color=GREY)
            .set_stroke(opacity=0.4)
            .rotate(PI / 2)
        )

        gm_dt_tip = Dot(UL, color=YELLOW)
        gm_tr_path = TracedPath(
            gm_dt_tip.get_center,
            dissipating_time=0.5,
            stroke_opacity=[0, 1],
            stroke_color=YELLOW,
            stroke_width=2,
        )
        self.add(gm_tr_path)

        tx_haz_esto = Tex(
            R"""
            Haz algo...
            """,
            font_size=44,
        ).next_to(tx_for_while, DOWN, buff=0.5)

        tx_condition = Tex(
            R"""
            \textbf{\textit{condición}}
            """,
            font_size=27,
            color=GREEN,
        ).next_to(tx_for_while, DOWN, buff=0.5)

        self.wait(5)

        self.play(Write(tx_haz_esto))
        self.wait(1)

        self.play(
            tx_haz_esto.animate.scale(0.7).move_to(ORIGIN).set_opacity(0.4),
            Create(gm_circle),
            run_time=1,
        )
        self.wait(4)
        self.play(Write(tx_condition))
        self.play(tx_condition.animate.move_to([0, 1.5, 0]))
        self.wait(4)

        for i in range(5):
            self.play(Indicate(tx_condition), run_time=0.4)
            gm_dt_tip.set_opacity(1)
            self.play(
                MoveAlongPath(gm_dt_tip, gm_circle, rate_func=linear),
                gm_circle.animate(run_time=0.05).set_stroke(color=YELLOW),
                tx_haz_esto.animate.set_opacity(1),
                run_time=1,
            )
            self.play(
                tx_haz_esto.animate.set_opacity(0.4),
                gm_circle.animate(run_time=0.05).set_stroke(color=WHITE),
                FadeOut(gm_dt_tip),
                run_time=0.5,
            )
        self.play(
            Indicate(tx_condition, color=RED, run_time=0.7),
        )
        tx_condition.set_color(RED),
        self.wait(2)
        self.play(
            FadeOut(tx_haz_esto, run_time=0.7),
            FadeOut(gm_circle, run_time=0.7),
            FadeOut(tx_condition, run_time=0.7),
            FadeOut(tx_for_while, run_time=0.7),
        )
        self.wait(5)
        tx_practico = Tex(
            R"""
            Ahora un ejemplo práctico
            """
        )

        self.play(Write(tx_practico))
        self.wait(20)
        self.play(FadeOut(tx_practico))
        self.wait(4)

        gm_sq = Square(4, color=PURPLE).to_edge(LEFT, buff=0.5)

        tx_ejem_cond = Tex(
            R"""
            \textbf{$x > 20$}
            """,
            font_size=32,
            color=GREEN,
        ).move_to([0, 1.5, 0])

        tx_init = Tex(
            R"""
            \textbf{Inicializa x = 0}
            """,
            font_size=30,
        ).move_to(gm_sq.get_center())

        gm_sq.to_edge(RIGHT, buff=0.5)
        tx_imprime = Tex(
            R"""
            \textbf{Imprime x}
            """,
            font_size=30,
        ).move_to(gm_sq.get_center())

        tx_x_mas = Tex(
            R"""
            \textbf{x = x + 1}
            """,
            font_size=32,
        )

        gm_sq.to_edge(LEFT, buff=0.5)

        gm_arr_1 = (
            Arrow(start=ORIGIN, end=[1.3, 0, 0])
            .move_to([-2.5, 0, 0])
            .set_stroke(opacity=0.4)
        )
        gm_arr_2 = (
            Arrow(start=ORIGIN, end=[1.3, 0, 0])
            .move_to([2.5, 0, 0])
            .set_stroke(opacity=0.4)
        )

        vt_x = ValueTracker(0)
        tx_x = always_redraw(
            lambda: Tex(f"$x = {int(vt_x.get_value())}$", font_size=44).to_edge(
                UP, buff=1
            )
        )

        # rs
        self.play(
            Succession(
                Write(tx_init),
                Wait(3),
                Write(gm_arr_1, run_time=0.3),
                Write(tx_ejem_cond),
                Write(tx_x_mas),
                Write(gm_circle),
                Wait(5),
                Write(gm_arr_2, run_time=0.2),
                Write(tx_imprime),
                Wait(4),
                Write(tx_x),
            )
        )

        self.wait(2)

        self.play(
            Write(gm_sq),
        )

        self.add(gm_tr_path)

        self.play(Wiggle(gm_sq))
        self.play(
            gm_sq.animate.move_to(gm_circle.get_center()),
        )

        self.play(Wiggle(gm_sq))

        for i in range(4):
            self.play(Indicate(tx_ejem_cond), run_time=0.2)
            self.add(gm_dt_tip, gm_tr_path)
            self.play(
                MoveAlongPath(gm_dt_tip, gm_circle, rate_func=linear),
                gm_circle.animate(run_time=0.05).set_stroke(color=YELLOW),
                tx_x_mas.animate.set_opacity(1),
                run_time=0.7,
            )
            vt_x.set_value(vt_x.get_value() + 1)
            self.play(
                tx_x_mas.animate.set_opacity(0.4),
                gm_circle.animate(run_time=0.05).set_stroke(color=WHITE),
                run_time=0.2,
            )

        def easeInOutSine(x: float) -> float:
            return 0.5 * (1 - cos(PI * x))

        cur = vt_x.get_value()
        self.remove(gm_tr_path)
        flag = True
        gm_circle.set_stroke(color=YELLOW)
        for i in range(int(cur), 20):

            progress = vt_x.get_value() / 20.0
            f = easeInOutSine(progress)  # Apply the easing function
            f *= 0.005  # Scale the easing factor if necessary

            self.play(Indicate(tx_ejem_cond), run_time=0.4 * f)
            self.play(
                MoveAlongPath(gm_dt_tip, gm_circle, rate_func=linear),
                tx_x_mas.animate.set_opacity(1),
                run_time=0.2,
            )
            vt_x.set_value(vt_x.get_value() + 1)
            tx_x_mas.set_opacity(0.4),

        self.play(
            Indicate(tx_ejem_cond, color=RED),
            gm_circle.animate.set_color(RED),
            tx_x_mas.animate.set_color(RED),
            gm_dt_tip.animate.set_color(RED),
        )
        tx_ejem_cond.set_color(RED)

        self.play(gm_sq.animate.move_to(tx_imprime.get_center()))
        self.play(Wiggle(gm_sq))

        self.wait(5)


class ForVsWhile(Scene):
    def construct(self):

        tx_ti = Tex("El for vs el while", font_size=60)
        self.play(Write(tx_ti))
        self.wait(3)
        self.play(Uncreate(tx_ti))
        self.wait(1)

        tx_for = Tex(
            r"""
            \underline{\textbf{for}}
            """,
            font_size=40,
        ).shift(UP * 2 + LEFT * 2.2)

        tx_ls_for = Tex(
            r"""
            \begin{enumerate} 
                \setlength{\itemsep}{0.1cm}
                \item Número de iteraciones definido.
                \item Recorrer arreglos, vectores, etc...
                \item Iterar sobre un rango de números.
                \item Recorrer una string.
            \end{enumerate}
            """,
            font_size=22,
        ).next_to(tx_for, DOWN, buff=0.3)

        tx_while = Tex(
            r"""
            \underline{\textbf{while}}
            """,
            font_size=40,
        ).shift(UP * 2 + RIGHT * 2.2)
        tx_ls_while = Tex(
            r"""
            \begin{enumerate} 
                \setlength{\itemsep}{0.1cm}
                \item Número de iteraciones desconocido.
                \item Recorrer grafos.
                \item Recibir input.
                \item Leer archivos.
            \end{enumerate}
            """,
            font_size=22,
        ).next_to(tx_while, DOWN, buff=0.3)

        self.play(
            Write(tx_for),
            Write(tx_ls_for, run_time=5),
        )
        self.wait(15)
        self.play(
            Write(tx_while),
            Write(tx_ls_while, run_time=5),
        )
        self.wait(15)

        gp = VGroup()
        gp += tx_ls_for
        gp += tx_for
        gp += tx_while
        gp += tx_ls_while
        self.play(FadeOut(gp))
        self.wait(5)


class test(Scene):
    def construct(self):
        vt_x = ValueTracker(0)
        gm_arc = ArcBetweenPoints(
            start=UR, end=UL, angle=-6 / 4 * PI, stroke_color=YELLOW
        )

        tx_x = always_redraw(
            lambda: Tex(f"{int(vt_x.get_value())}", font_size=46).to_corner(
                UL, buff=0.5
            )
        )
        self.add(tx_x)
        gm_dt_tip = Dot(UL, color=YELLOW)
        gm_dt_tip.add_updater(lambda d: d.move_to(gm_arc.get_end()))
        self.add(gm_dt_tip)
        self.play(vt_x.animate.set_value(10))
        self.wait()
        ApplyMethod
