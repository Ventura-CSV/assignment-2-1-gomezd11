def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = 40
    num_females = 60

    total_students = num_males + num_females

    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100

    print("number of students " + str(total_students))
    print(f"Percentage of males: {m_perc:.2f}%")
    print(f"Percentage of females: {f_perc:.2f}%")
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
