import javax.swing.JFrame; //gonna open the frame and IS the calculator visual 
import javax.swing.JTextField; 
import java.awt.BorderLayout; //awt is older than swing and it helps pick where everything goes inside the window
import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.GridLayout;
public class Calculator {
    public static void main(String[] args) {
        //opening and setting the calc box
        JFrame window= new JFrame("Calculator");
        window.setSize(300,400);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JTextField display= new JTextField("0");
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT); //puts the 0 on the right side
        window.add(display, BorderLayout.NORTH); //put these last 3 three lines before setVisible so all this shows up
       
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 4, 5, 5));
        String[] buttons = {"7","8","9","/",
                    "4","5","6","*",
                    "1","2","3","-",
                    "C","0","=","+"};

        for (String label : buttons) {
            JButton btn = new JButton(label);
            buttonPanel.add(btn);
        }

        window.add(buttonPanel, BorderLayout.CENTER);

        window.setVisible(true);
      

    }
    




}