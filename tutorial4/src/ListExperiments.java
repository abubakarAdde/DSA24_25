import java.util.*;
public class ListExperiments {
    public static void main(String[] args) {
        //ArrayList<String> myList = new ArrayList<String>();
        LinkedList<String> mylist = new LinkedList<>();
        demonstrateList(mylist);

    }
        public static void demonstrateList(LinkedList<String> list) {
            list.add("Apples");
            list.add("Oranges");
            list.add("Bananas");
            System.out.println( list);

            list.add(1, "Pineapples");
            System.out.println( list);

            list.remove(2);
            System.out.println( list);
            System.out.println( list.size());
        }






}