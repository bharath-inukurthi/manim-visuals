from manim import *
import numpy as np

class ForwardPropagationDemo(Scene):
    def construct(self):
        # Color definitions
        WHITE = "#FFFFFF"
        CYAN = "#00FFFF"
        LIGHT_GREY = "#CCCCCC"
        YELLOW = "#FFD700"
        
        # Coordinate system: (0,0) to (100,100) grid
        def to_screen_coords(x, y):
            # Convert from (0,100) grid to Manim coordinates
            return np.array([(x - 50) * 0.14, (50 - y) * 0.08, 0])
        
        # Create nodes
        input_nodes = []
        hidden_nodes = []
        output_node = None
        
        # Input nodes at (15, 30), (15, 50), (15, 70)
        input_positions = [(15, 30), (15, 50), (15, 70)]
        for i, pos in enumerate(input_positions):
            node = Circle(radius=0.25, color=WHITE)
            node.move_to(to_screen_coords(pos[0], pos[1]))
            input_nodes.append(node)
        
        # Hidden nodes at (50, 30), (50, 50), (50, 70)
        hidden_positions = [(50, 30), (50, 50), (50, 70)]
        for i, pos in enumerate(hidden_positions):
            node = Circle(radius=0.25, color=WHITE)
            node.move_to(to_screen_coords(pos[0], pos[1]))
            hidden_nodes.append(node)
        
        # Output node at (85, 50)
        output_node = Circle(radius=0.25, color=WHITE)
        output_node.move_to(to_screen_coords(85, 50))
        
        # Part 1: Network & Input Setup (0:00 - 0:08)
        
        # (0:01) APPEAR: All Nodes
        self.play(
            *[FadeIn(node) for node in input_nodes + hidden_nodes + [output_node]],
            run_time=2
        )
        
        # (0:03) APPEAR: Column Labels
        input_label = Text("INPUT", color=WHITE, font_size=24)
        input_label.move_to(to_screen_coords(15, 10))
        
        hidden_label = Text("HIDDEN", color=WHITE, font_size=24)
        hidden_label.move_to(to_screen_coords(50, 10))
        
        output_label = Text("OUTPUT", color=WHITE, font_size=24)
        output_label.move_to(to_screen_coords(85, 10))
        
        self.play(
            FadeIn(input_label),
            FadeIn(hidden_label),
            FadeIn(output_label),
            run_time=2
        )
        
        # (0:05) DISAPPEAR: Column Labels
        self.play(
            FadeOut(input_label),
            FadeOut(hidden_label),
            FadeOut(output_label),
            run_time=1
        )
        
        # (0:06) APPEAR: Input Values
        input_values = []
        input_texts = ["0.5", "0.8", "0.2"]
        for i, (node, text) in enumerate(zip(input_nodes, input_texts)):
            value_text = Text(text, color=CYAN, font_size=16)
            value_text.move_to(node.get_center())
            input_values.append(value_text)
        
        self.play(
            *[FadeIn(value) for value in input_values],
            run_time=1
        )
        
        # (0:07) APPEAR: Vector Label
        # Create brackets around input nodes
        bracket_left = Text("[", color=CYAN, font_size=36)
        bracket_left.move_to(to_screen_coords(8, 50))
        
        bracket_right = Text("]", color=CYAN, font_size=36)
        bracket_right.move_to(to_screen_coords(22, 50))
        
        vector_label = Text("Input Vector x", color=CYAN, font_size=20)
        vector_label.move_to(to_screen_coords(15, 85))
        
        self.play(
            FadeIn(bracket_left),
            FadeIn(bracket_right),
            FadeIn(vector_label),
            run_time=1
        )
        
        # Part 2: Calculating Hidden Node 1 (0:09 - 0:17)
        
        # (0:09) ACTION: Isolate Calculation
        # Focus on the calculation without dimming other elements
        run_time=1
        
        # (0:10) APPEAR: Connections & Weights
        connections = []
        weights = []
        weight_values = ["w₁₃ = 0.2", "w₂₃ = 0.4", "w₃₃ = -0.3"]
        
        for i, (input_node, weight_text) in enumerate(zip(input_nodes, weight_values)):
            # Create connection line
            line = Line(
                input_node.get_center(),
                hidden_nodes[2].get_center(),
                color=WHITE,
                stroke_width=2
            )
            connections.append(line)
            
            # Create weight text positioned just above the connection line
            weight = Text(weight_text, color=WHITE, font_size=16)
            # Position weight at midpoint of connection line, but slightly above
            start_pos = input_node.get_center()
            end_pos = hidden_nodes[2].get_center()
            mid_point = (start_pos + end_pos) / 2
            
            # Calculate angle to rotate weight text to match connection line
            angle = np.arctan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
            
            # Move weight slightly above the connection line
            offset_distance = 0.15  # Distance above the line
            offset_x = -offset_distance * np.sin(angle)
            offset_y = offset_distance * np.cos(angle)
            weight.move_to(mid_point + np.array([offset_x, offset_y, 0]))
            
            weight.rotate(angle)
            
            weights.append(weight)
        
        self.play(
            *[Create(line) for line in connections],
            *[FadeIn(weight) for weight in weights],
            run_time=2
        )
        
        # (0:12) ANIMATION: Show Weighted Sum
        # Make input values and weights stand out
        self.play(
            *[value.animate.set_color(CYAN) for value in input_values],
            *[weight.animate.set_color(WHITE) for weight in weights],
            run_time=1
        )
        
        # Show calculation with individual colored terms
        # Create separate text objects for each multiplication term
        calc_part1 = Text("Sum = (", color=LIGHT_GREY, font_size=18)
        calc_part2 = Text("0.5 × 0.2", color="#FF6B6B", font_size=18)  # Red
        calc_part3 = Text(") + (", color=LIGHT_GREY, font_size=18)
        calc_part4 = Text("0.8 × 0.4", color="#4ECDC4", font_size=18)  # Cyan
        calc_part5 = Text(") + (", color=LIGHT_GREY, font_size=18)
        calc_part6 = Text("0.2 × -0.3", color="#45B7D1", font_size=18)  # Blue
        calc_part7 = Text(")", color=LIGHT_GREY, font_size=18)
        
        # Position the calculation parts
        calc_parts = [calc_part1, calc_part2, calc_part3, calc_part4, calc_part5, calc_part6, calc_part7]
        calc_group = VGroup(*calc_parts).arrange(RIGHT, buff=0.1)
        calc_group.move_to(to_screen_coords(50, 85))
        
        self.play(
            FadeIn(calc_group),
            run_time=2
        )
        
        # Upscale first multiplication term
        self.play(
            calc_part2.animate.scale(1.3).set_color("#FF6B6B"),  # Red
            input_values[0].animate.set_color("#FF6B6B").scale(1.2),
            weights[0].animate.set_color("#FF6B6B").scale(1.2),
            run_time=0.8
        )
        self.play(
            calc_part2.animate.scale(1/1.3),
            input_values[0].animate.scale(1/1.2),
            weights[0].animate.scale(1/1.2),
            run_time=0.8
        )
        # Upscale second multiplication term
        self.play(
            calc_part4.animate.scale(1.3).set_color("#4ECDC4"),  # Cyan
            input_values[1].animate.set_color("#4ECDC4").scale(1.2),
            weights[1].animate.set_color("#4ECDC4").scale(1.2),
            run_time=0.8
        )
        self.play(
            calc_part4.animate.scale(1/1.3),
            input_values[1].animate.scale(1/1.2),
            weights[1].animate.scale(1/1.2),
            run_time=0.8
        )
        # Upscale third multiplication term
        self.play(
            calc_part6.animate.scale(1.3).set_color("#FFD93D"),  # Yellow
            input_values[2].animate.set_color("#FFD93D").scale(1.2),
            weights[2].animate.set_color("#FFD93D").scale(1.2),
            run_time=0.8
        )
        self.play(
            calc_part6.animate.scale(1/1.3),
            input_values[2].animate.scale(1/1.2),
            weights[2].animate.scale(1/1.2),
            run_time=0.8
        )
        
        # (0:14) ANIMATION: Add Bias
        result_text = Text("Sum = 0.36", color=LIGHT_GREY, font_size=18)
        result_text.move_to(to_screen_coords(50, 85))
        
        bias_text = Text("Bias b₃ = -0.1", color=LIGHT_GREY, font_size=18)
        bias_text.move_to(to_screen_coords(50, 75))
        
        final_calc = Text("z₃ = 0.36 + (-0.1) = 0.26", color=LIGHT_GREY, font_size=18)
        final_calc.move_to(to_screen_coords(50, 85))
        
        self.play(
            Transform(calc_group, result_text),
            FadeIn(bias_text),
            run_time=1
        )
        
        self.play(
            Transform(calc_group, final_calc),
            run_time=2
        )
        
        # (0:17) DISAPPEAR: Weights
        self.play(
            *[FadeOut(weight) for weight in weights],
            run_time=1
        )
        
        # Part 3: Activation of Hidden Node 1 (0:18 - 0:24)
        
        # (0:18) APPEAR: Sigmoid Graph
        # Create sigmoid function
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=3,
            y_length=2,
            axis_config={"color": YELLOW}
        )
        axes.move_to(to_screen_coords(75, 30))
        
        sigmoid = axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=YELLOW)
        
        # Add sigmoid formula
        sigmoid_formula = Text(
            "σ(x) = 1 / (1 + e^(-x))",
            color=YELLOW,
            font_size=14
        )
        sigmoid_formula.move_to(to_screen_coords(75, 15))
        
        self.play(
            Create(axes),
            Create(sigmoid),
            FadeIn(sigmoid_formula),
            run_time=2
        )
        
        # Upscale sigmoid formula
        self.play(
            sigmoid_formula.animate.scale(1.2),
            run_time=0.3
        )
        
        self.play(
            sigmoid_formula.animate.scale(1/1.2),
            run_time=0.3
        )
        
        # (0:20) ANIMATION: Apply Function
        # Create dot that moves along sigmoid
        dot = Dot(color=YELLOW, radius=0.05)
        dot.move_to(axes.c2p(0.26, 0.56))
        
        # Create path for dot movement
        path = VMobject()
        path.set_points_as_corners([
            calc_group.get_center(),
            axes.c2p(0.26, 0),
            axes.c2p(0.26, 0.56)
        ])
        
        self.play(
            MoveAlongPath(dot, path),
            run_time=2
        )
        
        # (0:22) ANIMATION: Set Node Value
        # Move dot to hidden node
        path_to_node = Line(dot.get_center(), hidden_nodes[2].get_center())
        
        # Create value text for hidden node
        hidden_value = Text("0.56", color=YELLOW, font_size=16)
        hidden_value.move_to(hidden_nodes[2].get_center())
        
        self.play(
            MoveAlongPath(dot, path_to_node),
            FadeIn(hidden_value),
            run_time=2
        )
        
        # (0:24) DISAPPEAR: Cleanup
        self.play(
            FadeOut(axes),
            FadeOut(sigmoid),
            FadeOut(sigmoid_formula),
            FadeOut(dot),
            *[FadeOut(line) for line in connections],
            FadeOut(calc_group),
            FadeOut(bias_text),
            run_time=1
        )
        
        # Part 4: Completing the Hidden Layer (0:25 - 0:26)
        
        # (0:25) ACTION: Quick Populate & Restore
        # Continue with next step
        run_time=0.5
        
        # Flash of connections and values
        flash_lines = []
        for i, input_node in enumerate(input_nodes):
            for j, hidden_node in enumerate(hidden_nodes):
                if j != 2:  # Skip the one we already calculated
                    line = Line(
                        input_node.get_center(),
                        hidden_node.get_center(),
                        color=WHITE,
                        stroke_width=1
                    )
                    flash_lines.append(line)
        
        # Create values for other hidden nodes
        other_values = []
        other_texts = ["0.34", "0.82"]
        for i, (node, text) in enumerate(zip(hidden_nodes[:2], other_texts)):
            value = Text(text, color=YELLOW, font_size=16)
            value.move_to(node.get_center())
            other_values.append(value)
        
        self.play(
            *[Create(line) for line in flash_lines],
            run_time=0.3
        )
        
        self.play(
            *[FadeOut(line) for line in flash_lines],
            *[FadeIn(value) for value in other_values],
            run_time=0.3
        )
        
        # Part 5: Output Calculation (0:27 - 0:33)
        
        # (0:27) ACTION: Isolate Output
        # Focus on output calculation
        run_time=1
        
        # (0:28) APPEAR: Final Connections & Weights
        output_connections = []
        output_weights = []
        weight_texts = ["wₒ₁ = 0.9", "wₒ₂ = -0.5", "wₒ₃ = 0.7"]
        
        for i, (hidden_node, weight_text) in enumerate(zip(hidden_nodes, weight_texts)):
            # Create connection line
            line = Line(
                hidden_node.get_center(),
                output_node.get_center(),
                color=WHITE,
                stroke_width=2
            )
            output_connections.append(line)
            
            # Create weight text positioned just above the connection line
            weight = Text(weight_text, color=WHITE, font_size=16)
            # Position weight at midpoint of connection line, but slightly above
            start_pos = hidden_node.get_center()
            end_pos = output_node.get_center()
            mid_point = (start_pos + end_pos) / 2
            
            # Calculate angle to rotate weight text to match connection line
            angle = np.arctan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
            
            # Move weight slightly above the connection line
            offset_distance = 0.15  # Distance above the line
            offset_x = -offset_distance * np.sin(angle)
            offset_y = offset_distance * np.cos(angle)
            weight.move_to(mid_point + np.array([offset_x, offset_y, 0]))
            
            weight.rotate(angle)
            
            output_weights.append(weight)
        
        self.play(
            *[Create(line) for line in output_connections],
            *[FadeIn(weight) for weight in output_weights],
            run_time=2
        )
        
        # (0:30) ANIMATION: Show Final Weighted Sum & Bias
        final_calc_text = Text(
            "zₒ = (0.34×0.9) + (0.82×-0.5) + (0.56×0.7) + 0.2 = 0.488",
            color=LIGHT_GREY,
            font_size=16
        )
        final_calc_text.move_to(to_screen_coords(50, 5))
        # Create colored terms for output calculation
        out_term1 = Text("0.34×0.9", color="#FF6B6B", font_size=16)
        out_term2 = Text("0.82×-0.5", color="#4ECDC4", font_size=16)
        out_term3 = Text("0.56×0.7", color="#FFD93D", font_size=16)
        out_plus1 = Text(" + ", color=LIGHT_GREY, font_size=16)
        out_plus2 = Text(" + ", color=LIGHT_GREY, font_size=16)
        out_plus3 = Text(" + 0.2 = 0.488", color=LIGHT_GREY, font_size=16)
        out_calc_group = VGroup(out_term1, out_plus1, out_term2, out_plus2, out_term3, out_plus3).arrange(RIGHT, buff=0.08)
        out_calc_group.move_to(to_screen_coords(50, 5))
        self.play(FadeIn(out_calc_group), run_time=1)
        # Animate each output multiplication term and corresponding hidden node/weight
        self.play(
            out_term1.animate.scale(1.3).set_color("#FF6B6B"),
            other_values[0].animate.set_color("#FF6B6B").scale(1.2),
            output_weights[0].animate.set_color("#FF6B6B").scale(1.2),
            run_time=0.7
        )
        self.play(
            out_term1.animate.scale(1/1.3),
            other_values[0].animate.scale(1/1.2),
            output_weights[0].animate.scale(1/1.2),
            run_time=0.7
        )
        self.play(
            out_term2.animate.scale(1.3).set_color("#4ECDC4"),
            other_values[1].animate.set_color("#4ECDC4").scale(1.2),
            output_weights[1].animate.set_color("#4ECDC4").scale(1.2),
            run_time=0.7
        )
        self.play(
            out_term2.animate.scale(1/1.3),
            other_values[1].animate.scale(1/1.2),
            output_weights[1].animate.scale(1/1.2),
            run_time=0.7
        )
        self.play(
            out_term3.animate.scale(1.3).set_color("#FFD93D"),
            hidden_value.animate.set_color("#FFD93D").scale(1.2),
            output_weights[2].animate.set_color("#FFD93D").scale(1.2),
            run_time=0.7
        )
        self.play(
            out_term3.animate.scale(1/1.3),
            hidden_value.animate.scale(1/1.2),
            output_weights[2].animate.scale(1/1.2),
            run_time=0.7
        )
        
       
        # (0:33) DISAPPEAR: Weights
        self.play(
            *[FadeOut(weight) for weight in output_weights],
            run_time=1
        )
        
        # Part 6: Final Prediction (0:34 - 0:43)
        
        # (0:34) APPEAR: Sigmoid Graph
        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=3,
            y_length=2,
            axis_config={"color": YELLOW}
        )
        axes2.move_to(to_screen_coords(75, 30))
        
        sigmoid2 = axes2.plot(lambda x: 1 / (1 + np.exp(-x)), color=YELLOW)
        
        # Add sigmoid formula for final activation
        sigmoid_formula2 = Text(
            "σ(x) = 1 / (1 + e^(-x))",
            color=YELLOW,
            font_size=14
        )
        sigmoid_formula2.move_to(to_screen_coords(75, 15))
        
        self.play(
            Create(axes2),
            Create(sigmoid2),
            FadeIn(sigmoid_formula2),
            run_time=1
        )
        
        # Upscale final sigmoid formula
        self.play(
            sigmoid_formula2.animate.scale(1.2),
            run_time=0.3
        )
        
        self.play(
            sigmoid_formula2.animate.scale(1/1.2),
            run_time=0.3
        )
        
        # (0:35) ANIMATION: Apply Function
        dot2 = Dot(color=YELLOW, radius=0.05)
        dot2.move_to(axes2.c2p(0.488, 0.62))
        
        path2 = VMobject()
        path2.set_points_as_corners([
            final_calc_text.get_center(),
            axes2.c2p(0.488, 0),
            axes2.c2p(0.488, 0.62)
        ])
        
        self.play(
            MoveAlongPath(dot2, path2),
            run_time=2
        )
        
        # (0:37) ANIMATION: Set Final Value
        path_to_output = Line(dot2.get_center(), output_node.get_center())
        
        output_value = Text("0.62", color=YELLOW, font_size=16)
        output_value.move_to(output_node.get_center())
        
        self.play(
            MoveAlongPath(dot2, path_to_output),
            FadeIn(output_value),
            run_time=2
        )
        
        # (0:39) DISAPPEAR: Final Cleanup
        self.play(
            FadeOut(axes2),
            FadeOut(sigmoid2),
            FadeOut(sigmoid_formula2),
            FadeOut(dot2),
            *[FadeOut(line) for line in output_connections],
            FadeOut(final_calc_text),
            run_time=1
        )
        
        # (0:40) APPEAR: Final Prediction Label
        prediction_box = Rectangle(
            width=0.6,
            height=0.6,
            color=YELLOW,
            stroke_width=3
        )
        prediction_box.move_to(output_node.get_center())
        
        prediction_label = Text("Final Prediction", color=YELLOW, font_size=20)
        prediction_label.move_to(to_screen_coords(85, 20))
        
        self.play(
            Create(prediction_box),
            FadeIn(prediction_label),
            run_time=1
        )
        
        # (0:41) APPEAR: Narration Text
        narration = Text(
            "And that is forward propagation. A simple, repeatable process of math that turns an input vector into a meaningful prediction.",
            color=WHITE,
            font_size=16,
            line_spacing=0.8
        )
        narration.move_to(to_screen_coords(50, 90))
        
        self.play(
            FadeIn(narration),
            run_time=2
        )
        
        # (0:43) Fade to black
        self.play(
            FadeOut(Group(*self.mobjects)),
            run_time=2
        )
