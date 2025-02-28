import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Pencil, Trash } from "lucide-react";

export default function TodoListApp() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");
  const [editingIndex, setEditingIndex] = useState(null);
  const [editText, setEditText] = useState("");

  useEffect(() => {
    const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
    setTasks(savedTasks);
  }, []);

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }, [tasks]);

  const addTask = () => {
    if (newTask.trim() === "") return;
    setTasks([...tasks, { text: newTask, completed: false }]);
    setNewTask("");
  };

  const toggleCompletion = (index) => {
    const updatedTasks = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(updatedTasks);
  };

  const deleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  const editTask = (index) => {
    setEditingIndex(index);
    setEditText(tasks[index].text);
  };

  const saveEdit = (index) => {
    const updatedTasks = tasks.map((task, i) =>
      i === index ? { ...task, text: editText } : task
    );
    setTasks(updatedTasks);
    setEditingIndex(null);
  };

  return (
    <div className="max-w-md mx-auto p-4 space-y-4">
      <h1 className="text-2xl font-bold text-center">To-Do List</h1>
      <div className="flex space-x-2">
        <Input
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Add a new task"
        />
        <Button onClick={addTask}>Add</Button>
      </div>
      <div className="space-y-2">
        {tasks.map((task, index) => (
          <Card key={index} className="flex items-center justify-between p-2">
            <div className="flex items-center space-x-2">
              <Checkbox
                checked={task.completed}
                onCheckedChange={() => toggleCompletion(index)}
              />
              {editingIndex === index ? (
                <Input
                  value={editText}
                  onChange={(e) => setEditText(e.target.value)}
                />
              ) : (
                <span className={task.completed ? "line-through" : ""}>{task.text}</span>
              )}
            </div>
            <div className="flex space-x-2">
              {editingIndex === index ? (
                <Button size="icon" onClick={() => saveEdit(index)}>
                  ✅
                </Button>
              ) : (
                <Button size="icon" onClick={() => editTask(index)}>
                  <Pencil size={16} />
                </Button>
              )}
              <Button size="icon" onClick={() => deleteTask(index)}>
                <Trash size={16} />
              </Button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}
