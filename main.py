
def unigue_names(mentors):
    all_list = []
    for person in mentors:
        all_list.extend(person)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'



def supernames(mentors, courses):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            name_split = name.split()
            only_name = name_split[:-1]
            course_names += only_name
        mentors_names.append(course_names)
    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    return f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}"




def namesake(mentors, courses, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    for course in courses_list:
        names_list = []
        for mentor in course["mentors"]:
            names_list.append(mentor.split(" ")[0].strip())
        unique_names = sorted(list(set(names_list)))
        same_name_list = []
        for name in unique_names:
            if names_list.count(name) > 1:
                for name_and_last in course["mentors"]:
                    if name in name_and_last:
                        same_name_list.append(name_and_last)
        if len(same_name_list) > 0:
            return f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}'

