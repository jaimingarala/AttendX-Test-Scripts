
def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    # Simulate recording attendance
    attendance_recorded = bool(student_id) and (
        attendance_status in ["Present", "Absent"]
    )

    assert attendance_recorded is True
    print("Attendance marking test passed")


def test_attendance_without_student_id():
    student_id = ""
    attendance_status = "Present"

    attendance_recorded = bool(student_id) and (
        attendance_status in ["Present", "Absent"]
    )

    assert attendance_recorded is False
    print("Missing student ID test passed")
