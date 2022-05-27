package Automata;
import javax.swing.JOptionPane;

public class Automata {
int cont;
 boolean valido;
static char[] lista;

   public void inicio(){
        cont=0;
        valido=false;
        q0();
    }
  public static void main(String[] args) {    
        Automata aut=new Automata();
        String cadena=JOptionPane.showInputDialog ("Inicio del programa \n"+"Introduzca una cadena:");
        lista=cadena.toCharArray();
        aut.inicio();
        if(aut.valido){//condicional que entra en el estado de aceptacion
            System.out.println("La cadena es valida");
        }  
    }

    
    public void q0(){
        System.out.println("Ha llegado a q0");
        valido=false;
        if(cont<lista.length){
          if(lista[cont]=='0'||lista[cont]=='1'||lista[cont]=='2'|lista[cont]=='3'||lista[cont]=='4'||lista[cont]=='5'||lista[cont]=='6'||lista[cont]=='7'||lista[cont]=='8'||lista[cont]=='9'){
                    cont++;
                    q1();
            }
      }   
    }
    
    public void q1(){
        System.out.println("Ha llegado a q1");
        valido=false;
        if(cont<lista.length){
             if(lista[cont]=='0'||lista[cont]=='1'||lista[cont]=='2'|lista[cont]=='3'||lista[cont]=='4'||lista[cont]=='5'||lista[cont]=='6'||lista[cont]=='7'||lista[cont]=='8'||lista[cont]=='9'){
                cont++;
                q1();
            }else if(lista[cont]=='.'){  
                cont++;//
                q2();
            }
        }    
    }
    public void q2(){
        System.out.println("Ha llegado a q2");
        valido=false;
         if(cont<lista.length){
         if(lista[cont]=='0'||lista[cont]=='1'||lista[cont]=='2'|lista[cont]=='3'||lista[cont]=='4'||lista[cont]=='5'||lista[cont]=='6'||lista[cont]=='7'||lista[cont]=='8'||lista[cont]=='9'){
                cont++;
                q1();
          }
             }else{
            System.out.println("La cadena no es valida");
            System.exit(0);
}
}
}

  