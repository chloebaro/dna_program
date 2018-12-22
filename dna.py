def is_base_pair(base1, base2):
    """ (str, str) -> bool
    
    Precondition: base1 and base2 are both one-letter DNA bases.
    
    Return True iff the two bases are complementary.
    
    Examples:
    >>> is_base_pair("A", "T")
    True
    >>> is_base_pair("G", "C")
    True
    >>> is_base_pair("C", "G")
    True
    >>> is_base_pair("G", "A")
    False
    """
    
    bases = base1 + base2 
    bases = bases.upper()
    if(("A" in bases) and ("T" in bases)):
        return True
    elif(("G" in bases) and ("C" in bases)):
        return True
    else:
        return False

def is_dna(strand1, strand2):
    """ (str, str) -> bool
    
    Precondition: strand1 and strand2 have the same length and consist only of
    one-letter DNA bases.
    
    Return True iff the two strands of DNA are complimentary.
    
    Examples:
    >>> is_dna("A", "T")
    True
    >>> is_dna("AA", "TT")
    True
    >>> is_dna("ATGC", "TACG")
    True
    >>> is_dna("ATGC", "TAAA")
    False
    
    """
    
    for index in range(len(strand1)):
        if not(is_base_pair(strand1[index], strand2[index])):
            return False
    
    return True

def is_dna_palindrome(strand1, strand2):
    """ (str, str) -> bool
    
    Precondition: strand1 and strand2 are the same length and complimentary to 
    each other.
    
    Return True iff strand1 and strand2 are palindromes to each other.
    
    Examples: 
    >>> is_dna_palindrome("GGCC", "CCGG")
    True
    >>> is_dna_palindrome("GGATCC", "CCTAGG")
    True
    >>> is_dna_palindrome("GGATTC", "CCCCAA")
    False
    >>> is_dna_palindrome("A", "A")
    True
    
    """
    
    upper_s1 = strand1.upper()
    upper_s2 = strand2.upper()
    
    reverse_upper_s1 = ""
    #We will reverse the first strand. 
    index = len(upper_s1) - 1
    
    while(index > -1):
        reverse_upper_s1 = reverse_upper_s1 + upper_s1[index]
        index -= 1
    
    return reverse_upper_s1 == upper_s2

def restriction_sites(strand, rcgn_sequence):
    """ (str, str) -> list of int
    
    Return a list of all the indices where rcgn_sequence starts in strand.
    
    Examples:
    >>> restriction_sites("GAATTCCCAA", "GAATTC")
    [0]
    >>> restriction_sites("AGAATTCAAAGAATTCTTTGAATTC", "GAATTC")
    [1, 10, 19]
    >>> restriction_sites("GAATTCCC", "AACC")
    []
    
    """
    
    new_strand = strand
    sequence_length = len(rcgn_sequence)
    index_list = []
    chars_passed = 0
    
    """ The following code will find all the indices at which the rcgn_sequence
    occurs in the strand. We will change new_strand each time we find the 
    rcgn_sequence by removing everything before and including rcgn_sequence
    from new_strand (which is initially equal to strand). This process makes it 
    easier for us to find subsequent instances of rcgn_sequences in the strand.
    """
    while(rcgn_sequence in new_strand):
        index = new_strand.find(rcgn_sequence) + chars_passed
        index_list.append(index)
        chars_passed = chars_passed + new_strand.find(rcgn_sequence) +\
            sequence_length
        new_strand = new_strand[new_strand.find(rcgn_sequence) +\
                                sequence_length:]
    
    return index_list

def match_enzymes(strand, r_enzyme_names, recognition_sequences):
    """ (str, list of str, list of str) -> list of two item [str, list of int]
    lists
    
    Precondition: r_enzyme_names and recognition_sequences have the same length.
    
    Return a two item list that consists of each restriction enzyme name and
    the indices at which the restriction enzyme's corresponding recognition 
    sequence occurs.
    
    Examples:
    >>> strand = "AGAATTCGGATCCGAATTC"
    >>> r_enzyme_list = ["EcoRI", "BamHI"]
    >>> recog_sequences = ["GAATTC", "GGATCC"]
    >>> match_enzymes(strand, r_enzyme_list, recog_sequences)
    [["EcoRI", [1, 13]], ["BamHI", [7]]]
    >>> r_enzyme_list.append("HindIII")
    >>> recog_sequences.append("AAGCTT")
    >>> match_enzymes(strand, r_enzyme_list, recog_sequences)
    [["EcoRI", [1, 13]], ["BamHI", [7]], ["HindIII", []]]
    
    """
    
    
    enzyme_and_site_list = []
    for i in range(len(r_enzyme_names)):
        rstrcn_sites = restriction_sites(strand, recognition_sequences[i])
        enzyme_and_site = []
        enzyme_and_site.append(r_enzyme_names[i])
        enzyme_and_site.append(rstrcn_sites)
        enzyme_and_site_list.append(enzyme_and_site)
    
    return enzyme_and_site_list

def one_cutters(strand, r_enzyme_names, recognition_sequences):
    """ (str, list of str, list of str) -> list of two item [str, int] lists
    
    Precondition: r_enzyme_names and recognition_sequences have the same 
    length.
    
    Return a list of one-cutter names from r_enzyme_names and their 
    corresponding index at which they cut the strand. An enzyme is only a 
    one-cutter if it cuts the enzyme at exactly one place.
    
    Examples:
    >>> strand = "AGAATTCGGATCCGAATTC"
    >>> r_enzyme_list = ["EcoRI", "BamHI"]
    >>> recog_sequences = ["GAATTC", "GGATCC"]
    >>> one_cutters(strand, r_enzyme_list, recog_sequences)
    [["BamHI", 7]]
    >>> strand = "AGAATTCGGATCCGA"
    >>> one_cutters(strand, r_enzyme_list, recog_sequences)
    [["EcoRI", 1], ["BamHI", 7]]
    >>> strand = "AGAATTC"
    >>> one_cutters(strand, r_enzyme_list, recog_sequences)
    [["EcoRI", 1]]
    >>> strand = "AAAAAAAA"
    >>> one_cutters(strand, r_enzyme_list, recog_sequences)
    []
    
    """
    
    enzyme_and_site_list = match_enzymes\
        (strand, r_enzyme_names, recognition_sequences)
    one_cutter_list = []
    
    for item in enzyme_and_site_list:
        if len(item[1]) == 1: 
            one_cutter = []
            one_cutter.append(item[0])
            one_cutter.append(item[1][0])
            one_cutter_list.append(one_cutter)
    
    return one_cutter_list

def correct_mutations\
    (strand_list, clean_strand, r_enzyme_names, recognition_sequences):
    """ (list of str, str, list of str, list of str) -> NoneType
    
    Precondition: r_enzyme_names and recognition_sequences have the same length,
    and the clean_strand contains exactly one 1-cutter from r_enzyme_names.
    
    Return nothing. This function modifies strand_list (which is a list of 
    mutated DNA strands) to replace all the bases after the recognition sequence
    of the 1-cutter with bases after the 1-cutter's recognition sequence in the
    clean_strand. Note that if the clean strand's 1-cutter is not a 1-cutter for 
    the mutated strand, then the mutated strand is not changed.
    
    Examples: 
    >>> strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']
    >>> clean = 'ACGGCCTT'
    >>> names = ['HaeIII', 'HgaI', 'AluI']
    >>> sequences = ['GGCC', 'GACGC', 'AGCT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGCCTT', 'CAGCTGATCG']
    >>> strands = ['ACGTGGCCTAGCT', 'CAGCTGGCCACG']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGCCTT', 'CAGCTGGCCTT']
    >>> strands = ['AAAAGAATTC', 'AAGGGAAA']
    >>> clean = 'AAGAATTCA'
    >>> names = ['EcoRI', 'BamHI', 'HindIII']
    >>> sequences = ['GAATTC', 'GGATCC', 'AAGCTT']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['AAAAGAATTCA', 'AAGGGAAA']
    >>> strands = ['AAAAAAAA', 'GGGGGGGG']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['AAAAAAAA', 'GGGGGGGG']
    >>> strands = ['AGCTAGCTAAA', 'AAAAAA']
    >>> clean = 'AAAACGTA'
    >>> names = ['AluI', 'EcoRV', 'KpnI']
    >>> sequences = ['AGCT', 'GATATC', 'GGTACC']
    >>> correct_mutations(strands, clean, names, sequences)
    >>> strands
    ['AGCTAGCTAAA', 'AAAAAA']
    
    """
    
    clean_one_cutter = one_cutters\
        (clean_strand, r_enzyme_names, recognition_sequences)
    """ Note: clean_one_cutter will only consist of one [str, int] pair because 
    only one 1-cutter recognition sequence is present in clean_strand. """
    one_cutter_index = r_enzyme_names.index(clean_one_cutter[0][0])
    one_cutter_sequence = recognition_sequences[one_cutter_index]
    clean_beginning_index = clean_one_cutter[0][1] + len(one_cutter_sequence)
    """ The above variable represents the start index of the bases after the 
    one-cutter's recognition sequence in clean_strand. """
    if(clean_beginning_index < len(clean_strand)):    
        bases_to_add = clean_strand[clean_beginning_index:]
    else:
        bases_to_add = ""
        
    for index in range(len(strand_list)):
        mutated_one_cutter = one_cutters\
            (strand_list[index], [clean_one_cutter[0][0]], \
             [one_cutter_sequence]) 
        """ The above variable holds the one-cutters in the mutated strand. """
        if (one_cutter_sequence in strand_list[index]) \
           and len(mutated_one_cutter) > 0:
            """ The above if statement states that if the 1-cutter present in 
            the clean strand is also present and is a 1-cutter in the mutated 
            strand, we modify the mutated strand. """
            mutated_end_index = \
                strand_list[index].find(one_cutter_sequence) +\
                len(one_cutter_sequence)  
            strand_list[index] = strand_list[index][:mutated_end_index] +\
                bases_to_add
            """ The above statements replace the bases after the 1-cutter in the 
            mutated strand with the bases after the 1-cutter in the clean 
            strand. """


    