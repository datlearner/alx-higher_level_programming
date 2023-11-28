#include "lists.h"

/**
 * check_cycle - entry point
 * Description: check loop for lS
 * @list: * linked list
 * Return: 0 and 1
 */
int check_cycle(listint_t *list)
{
const listint_t *l = NULL, *list_two = NULL;
if (list == NULL)
return (0);
l = list;
list_two = list;
while (l && list_two && list_two->next)
{
l = l->next;
list_two = list_two->next->next;
if (l == list_two)
return (1);
}
return (0);
}
