from department import Department
import pytest


class TestDepartment:
    """Test cases for the Department class"""

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        """Drop tables prior to each test"""
        Department.drop_table()
        Department.all = {}

    def test_create_table(self):
        """Test create_table() method"""
        Department.create_table()
        assert Department.table_exists()

    def test_drop_table(self):
        """Test drop_table() method"""
        Department.create_table()
        Department.drop_table()
        assert not Department.table_exists()

    def test_save(self):
        """Test save() method"""
        Department.create_table()
        department = Department("Payroll", "Building A, 5th Floor")
        department.save()
        assert department.id is not None
        assert department.id in Department.all

    def test_create(self):
        """Test create() method"""
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        assert department.id is not None
        assert department.id in Department.all

    def test_update(self):
        """Test update() method"""
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        department.location = "Building B, 3rd Floor"
        department.update()
        updated_department = Department.find_by_id(department.id)
        assert updated_department.location == "Building B, 3rd Floor"

    def test_delete(self):
        """Test delete() method"""
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        department.delete()
        assert department.id not in Department.all

    def test_instance_from_db(self):
        """Test instance_from_db() method"""
        Department.create_table()
        department = Department("Payroll", "Building A, 5th Floor")
        department.save()
        fetched_department = Department.instance_from_db((department.id, department.name, department.location))
        assert fetched_department.id == department.id
        assert fetched_department.name == department.name
        assert fetched_department.location == department.location

    def test_get_all(self):
        """Test get_all() method"""
        Department.create_table()
        department1 = Department.create("Payroll", "Building A, 5th Floor")
        department2 = Department.create("Marketing", "Building B, 3rd Floor")
        departments = Department.get_all()
        assert len(departments) == 2
        assert department1 in departments
        assert department2 in departments

    def test_find_by_id(self):
        """Test find_by_id() method"""
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        found_department = Department.find_by_id(department.id)
        assert found_department == department

    def test_find_by_name(self):
        """Test find_by_name() method"""
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        found_department = Department.find_by_name(department.name)
        assert found_department == department